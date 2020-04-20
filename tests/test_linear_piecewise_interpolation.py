import pytest

from linear_piecewise_interpolation import Step

@pytest.mark.parametrize(
    'current, next, slope_truth', [
    # slope_truth is based on Python string casting,
    # a convenient way to compare floats in my opinion.
    (
        Step(start=0, data=[61,63,50,58], stepno=0),
        Step(start=30, data=[80,81,68,77], stepno=1),
        [0.6333333333333333, 0.6, 0.6, 0.6333333333333333]
    ),
    (
        Step(start=30, data=[80,81,68,77], stepno=1),
        Step(start=60, data=[62,63,52,60], stepno=2),
        [-0.6, -0.6, -0.5333333333333333, -0.5666666666666667]
    ),
    (
        Step(start=60, data=[62,63,52,60], stepno=2),
        Step(start=120, data=[83,82,70,79], stepno=3),
        [0.35, 0.31666666666666665, 0.3, 0.31666666666666665]
    )
    ])
def test_Step_process(current, next, slope_truth):
    current.process(next)
    assert current.end == next.start
    # Check the slope at a string precision level.
    assert str(current.slope) == str(slope_truth)
    # Check that the piecewise function intercepts the next point.
    for i in range(len(current.data)):
        assert(int(
                    current.data[i] +
                    (current.end - current.start) * current.slope[i]
                    )
                == int(next.data[i]))
