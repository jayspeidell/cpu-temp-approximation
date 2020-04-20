import pytest
from numpy import array, matmul, array_equal

from multiply import multiply

@pytest.mark.parametrize(
    'lhs, rhs', [
    # Random equal size example
    (
        array([
            [2,3,4,5],
            [4,1,4,6],
            [6,3,6,7],
            [8,7,6,5]]),
        array([
            [6,6,3,3],
            [7,4,8,2],
            [3,6,8,4],
            [9,8,3,5]])
    ),
    # Random mismatched size example
    (
        array([
            [2,6,2,5],
            [4,7,7,6],
            [6,8,3,7],
            [8,3,1,5]]),
        array([
            [6,3,3],
            [4,8,1],
            [6,3,4],
            [8,3,5]])
    ),
    # Quadratic Example Xt and X
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
    ),
    # Quadratic Example Xt and Y
    (
        array([
            [1,0,0],
            [1,1,1],
            [1,2,4]
        ]),
        array([
            [0],
            [1],
            [4]
        ])
    )
    ])
def test_multiply(lhs,rhs):
    assert array_equal(multiply(lhs, rhs), matmul(lhs, rhs))
