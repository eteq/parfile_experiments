class Schema(object):
    def __init__(self, nametotype):
        self._valdict = None
        self.names = list(nametotype.keys())
        self.types = nametotype.copy()

    def validate(self, valdict):
        for name, val in valdict.items():
            if name not in self.names:
                raise ValueError('parameter {} is not accepted by this schema'.format(name))

            if not isinstance(val, self.types[name]):
                raise ValueError('parameter {} is the wrong value.  Should be '
                                 '{} but is {}'.format(val, self.types[name], type(val)))

schemamap = {}

def schema(*args, **kwargs):
    if len(args)==1 and len(kwargs)==0:

        return _build_schema(args[0])
    else:
        return lambda f:_build_schema(f, *args, **kwargs)

def _build_schema(func, *args, **kwargs):
    import inspect

    global schemamap

    fargs, fvarargs, fvarkw, defaults = inspect.getargspec(func)
    if fvarargs is not None or fvarkw is not None:
        raise ValueError('Cannot make a schema from a varargs function')

    nametotype = {}
    rargs = args[::-1]
    for arg in fargs:
        if len(rargs)>0:
            nametotype[arg] = rargs.pop()
    for kw, val in kwargs.items():
        if kw in nametotype:
            raise ValueError('Both positional and kwarg given')
        if kw not in fargs:
            raise ValueError('Keyword {} is not an argument of the schema function'.format(kw))
        nametotype[kw] = val

    schemamap[func] = Schema(nametotype)

    return func


class Parset(object):
    def __init__(self, parfile, schema, target=None):
        self.target = target
        if hasattr(schema, 'validate'):
            self.schema = schema
        else:
            self.schema = schemamap[schema]
            if self.target is None:
                self.target = schema

        self._valdict = {}
        self.valdict = from_yaml(parfile)

    @property
    def valdict(self):
        dct = {}
        for nm in self._valnames:
            dct[nm] = getattr(self, nm)
        return dct
    @valdict.setter
    def valdict(self, invaldict):
        if self._valdict is not None:
            for nm in self._valdict:
                delattr(self, nm)

        for nm, val in invaldict.items():
            setattr(self, nm, val)
        self._valnames = list(invaldict.keys())

    def engage(self):
        self.schema.validate(self.valdict)
        self.target(**self.valdict)


def from_yaml(filename):
    """
    TEMPORARY
    """
    valdict = {}
    with open(filename) as f:
        for l in f:
            k, v = l.split(':')
            try:
                valdict[k.strip()] = float(v.strip())
            except ValueError:
                valdict[k.strip()] = v.strip()

    return valdict
