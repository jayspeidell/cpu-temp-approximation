import pytest

from linear_piecewise_interpolation import Step, piecewise_solver
import os
import glob
import filecmp
from parse_temps import (parse_raw_temps)
from numpy import array, append


@pytest.mark.parametrize(
    'current, next, slope_truth', [
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
    # slope_truth is based on Python string casting,
    # a convenient way to compare floats in my opinion.
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


@pytest.mark.parametrize(
    'input_file, output_files', [
    (
        'tests/test_data/piecewise_input.txt',
        [
            'Linear_Piecewise_Interpolation_Core_1.txt',
            'Linear_Piecewise_Interpolation_Core_2.txt',
            'Linear_Piecewise_Interpolation_Core_3.txt',
            'Linear_Piecewise_Interpolation_Core_4.txt'
        ]
    )
    ])
def test_piecewise_solver(input_file, output_files):
    # This test is more a sanity check that the program is working and
    # I did not break it. This is just a driver function.

    for f in glob.glob('tests/test_data/piecewise_out/*'):
        os.remove(f)

    input_temps = input_file
    includes_units = True

    index = []
    initialized = False
    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file, units=includes_units):
            if not initialized:
                index.append(temps_as_floats[0])
                data = array([temps_as_floats[1]])
                initialized = True
            else:
                index.append(temps_as_floats[0])
                data = append(data, [temps_as_floats[1]], axis=0)
    piecewise_solver(index, data, output='tests/test_data/piecewise_out/')

    for file in output_files:
        assert(filecmp.cmp(
            'tests/test_data/piecewise_out/' + file,
            'tests/test_data/piecewise_truth/' + file)
        )
