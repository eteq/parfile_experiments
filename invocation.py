import schema_example  # this schema gets created *on import* here
import astropfile

astropfile.engage('parfile_example')  # runs all the tasks in the file

parset = astropfile.edit_params('parfile_example') # pops up a GUI/Web page that can edit the file
parset.engage() # actually runs the thing


parset = astropfile.edit_params(schema_example.fit_gaussian_to_echelle1)  # same as above, but creates a GUI with the defaults
parset.engage()
parset.save('backup_param_file')  # maybe the GUI also allows saving, but this way you can be sure it happens
parset.engage_string() # creates a string with python code that can be exec-ed
parset  # in an ipython notebook, this would display them all in a pretty manner


# this could be done at the *command line*:
python -m astropfile parfile_example