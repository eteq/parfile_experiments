from astropfile import schema


@schema(centerwl_guess=float, sig_guess=float, amp_guess=float, echelle_order=int)
def fit_gaussian_to_echelle1(centerwl_guess, sig_guess, amp_guess, echelle_order):
    ...

# If there are defaults, guess the type based on what the defaults are
@schema(centerwl_guess=float)
def fit_gaussian_to_echelle2(centerwl_guess, sig_guess=0.5, amp_guess=1.0, echelle_order=5):
    ...

# But can always override if necessary
@schema(centerwl_guess=float, amp_guess=float)
def fit_gaussian_to_echelle3(centerwl_guess, sig_guess=0.5, amp_guess=1, echelle_order=5):
    ...

# Should also allow the possibility of more complicated objects getting passed in
@schema(center_guess=Quantity)
def fit_gaussian_to_echelle_Q1(center_guess, sig_guess=0.5*u.nm, amp_guess=1., echelle_order=5):
    # note that now center_guess doesn't have to be a wavelength - if the user passes in a frequency it could be 
    # auto-converted by this function, because Quantity has unit information baked in
    ...
    
# Bonus: allow Quantities to be specific physical types.  Astropy already has machinery to do this so we 
# could probably hook into that
from astropy import units as u

@schema(center_guess=u.angstrom)  # giving a unit implies a Quantity?
def fit_gaussian_to_echelle_Q2(center_guess, sig_guess=0.5*u.nm, amp_guess=1, echelle_order=5):
    # note that now center_guess doesn't have to be a wavelength - if the user passes in a frequency it could be 
    # auto-converted by this function, because Quantity has unit information baked in
    ...