"""Simple trapezoid-rule integrator."""

import numpy as np


def trapzf(f, a, b, npts=100):
    """Integrate a function using the trapezoid rule.

    Parameters
    ----------
    f : callable f(x)
        Function to integrate.
    a, b : float
        Interval over which to integrate `f`.
    npts : int, optional
        Number of equally spaced points at which to sample f at (between
        a and b).

    Returns
    -------
    float
        Integral of `f` over the interval `[a, b)`.
    """
    # Generate an equally spaced grid to sample the function.
    x = np.linspace(a, b, npts)

    # For an equispaced grid, the x spacing can just be read off from the
    # first two points and factored out of the summation.
    dx = x[1] - x[0]

    # Sample the input function at all values of x
    y = np.array([f(v) for v in x])

    # Compute the trapezoid rule sum for the final result
    return 0.5 * dx * (y[1:] + y[:-1]).sum()

