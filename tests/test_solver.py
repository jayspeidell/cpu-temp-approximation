
import pytest
from numpy import array, array_equal

from solver import solve, transpose

@pytest.mark.parametrize(
    'X, Xt, Y, PrintZero, coeffs, solution', [
    (
        array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ]),
        array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ]),
        array([
                [0],
                [1],
                [4]
            ]),
        True,
        [0.0,0.0,1.0],
        "phi_hat = 0.0 + 0.0 * x^1 + 1.0 * x^2"
    ),
    (
        array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ]),
        array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ]),
        array([
                [0],
                [1],
                [4]
            ]),
        False,
        [0.0,0.0,1.0],
        "phi_hat = 1.0 * x^2"
    )
])
def test_solve(X, Xt, Y, PrintZero, coeffs, solution):
    """
    The parameter Xt has been deprecated but remains available in testing. 
    """
    assert solve(X, Y, PrintZero)[0] == coeffs
    assert solve(X, Y, PrintZero)[1] == solution


@pytest.mark.parametrize(
    'X, Xt', [
    (
        array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ]),
        array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ]),
    ),
    (
        array([
                [1,0,0],
                [1,1,1],
                [1,2,4]
                ]),
        array([
                [1,1,1],
                [0,1,2],
                [0,1,4]
                ])
    )
])
def test_transpose(X, Xt):
    assert array_equal(transpose(X), Xt)
