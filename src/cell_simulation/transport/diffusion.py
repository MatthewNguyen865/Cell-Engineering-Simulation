def diffusion_rate(concentration_outside, concentration_inside, permeability):
    """
    Calculate transport rate across a membrane.

    Parameters
    ----------
    concentration_outside : float
        External concentration.

    concentration_inside : float
        Internal concentration.

    permeability : float
        Transport coefficient.

    Returns
    -------
    float
        Rate of transport into the cell.
    """

    return permeability * (
        concentration_outside - concentration_inside
    )