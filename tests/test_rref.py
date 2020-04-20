
import pytest
from numpy import array, matmul, array_equal, concatenate

from rref import rref, swap_rows, row_scale, eliminate, backsolve

@pytest.mark.parametrize(
    'lhs, rhs', [
    (
        array([
                [3,3,5,5],
                [3,5,9,9],
                [5,9,17,17]
            ]),
        array([
                [1,0,0,0],
                [0,1,0,0],
                [0,0,1,1]
        ])

    ),

    ])
def test_rref(lhs, rhs):
    print("Input:")
    print(lhs)
    print("Truth:")
    print(rhs)
    print("Result:")
    print(rref(lhs))
    assert array_equal(rref(lhs), rhs)

@pytest.mark.parametrize(
    'lhs, rhs, r1, r2', [
    (
        array([
            [1,1,1,1],
            [2,2,2,2],
            [3,3,3,3],
            [4,4,4,4]
        ]),
        array([
            [1,1,1,1],
            [4,4,4,4],
            [3,3,3,3],
            [2,2,2,2]
        ]),
        1,
        3
    )
])
def test_swap_rows(lhs, r1, r2, rhs):
    print("Input:")
    print(lhs)
    print("Truth:")
    print(rhs)
    print("Result:")
    print(swap_rows(lhs, r1, r2))
    assert array_equal(swap_rows(lhs, r1, r2), rhs)


@pytest.mark.parametrize(
    'lhs, rhs, row', [
    (
        array([
            [5,5,5,5],
            [2,2,2,2],
            [3,3,3,3],
            [4,4,4,4]
        ]),
        array([
            [5,5,5,5],
            [2,2,2,2],
            [3,3,3,3],
            [1,1,1,1]
        ]),
        3,
    )
])
def test_row_scale(lhs, row, rhs):
    print("Input:")
    print(lhs)
    print("Truth:")
    print(rhs)
    print("Result:")
    print(row_scale(lhs, row))
    assert array_equal(row_scale(lhs, row), rhs)


@pytest.mark.parametrize(
    'lhs, rhs, row', [
    (
        array([
            [5,5,5,5],
            [2,2,2,2],
            [0,0,1,1],
            [4,4,4,4]
        ]),
        array([
            [5,5,5,5],
            [2,2,2,2],
            [0,0,1,1],
            [4,4,0,0]
        ]),
        2,
    ),
        (
            array([
                [1,1,1,1],
                [2,2,2,2],
                [5,5,5,5],
                [4,4,4,4]
            ]),
            array([
                [1,1,1,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ]),
            0,
        )
])
def test_eliminate(lhs, rhs, row):
    print("Input:")
    print(lhs)
    print("Truth:")
    print(rhs)
    print("Result:")
    print(eliminate(lhs, row))
    assert array_equal(eliminate(lhs, row), rhs)


@pytest.mark.parametrize(
    'lhs, rhs', [
    (
        array([
            [1,5,5,5],
            [0,1,2,2],
            [0,0,1,4]
        ]),
        array([
            [1,0,0,15],
            [0,1,0,-6],
            [0,0,1,4]
        ])
    )
])
def test_backsolve(lhs, rhs):
    print("Input:")
    print(lhs)
    print("Truth:")
    print(rhs)
    print("Result:")
    print(backsolve(lhs))
    assert array_equal(backsolve(lhs), rhs)
