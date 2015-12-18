from astropfile import schema


@schema(centerwl_guess=float, echelle_order=int, filename=str)
def fit_echelle(centerwl_guess, echelle_order, filename):
    print('Would have run the task with:')
    print('centerwl_guess', centerwl_guess)
    print('echelle_order', echelle_order)
    print('filename', filename)
