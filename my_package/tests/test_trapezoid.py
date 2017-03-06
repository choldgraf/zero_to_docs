from my_package import trapezoid_integrate

from numpy.testing import assert_almost_equal


def square(x): return x**2


def test_square():
    "Test integrating the square() function."
    assert_almost_equal(trapezoid_integrate(square, 0, 1), 1./3, 4)


def test_square2():
    "Another test integrating the square() function."
    assert_almost_equal(trapezoid_integrate(square, 0, 3, 350), 9.0, 4)


