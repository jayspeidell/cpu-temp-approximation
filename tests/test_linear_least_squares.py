import pytest

import os
import glob
import filecmp
from linear_least_squares import linear_least_squares
from parse_temps import (parse_raw_temps)
from numpy import array, append, array_equal, allclose



@pytest.mark.parametrize(
    'input_file, output_files', [
    (
        'tests/test_data/piecewise_input.txt',
        [
            'Linear_Least_Squares_Core_1.txt',
            'Linear_Least_Squares_Core_2.txt',
            'Linear_Least_Squares_Core_3.txt',
            'Linear_Least_Squares_Core_4.txt'
        ]
    )
    ])
def test_linear_least_squares(input_file, output_files):
    # This test is more a sanity check that the program is working and
    # I did not break it. This is just a driver function.

    for f in glob.glob('tests/test_data/linear_least_squares_out/*'):
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
    linear_least_squares(index, data, output='tests/test_data/linear_least_squares_out/')

    for file in output_files:
        assert(filecmp.cmp(
            'tests/test_data/linear_least_squares_out/' + file,
            'tests/test_data/linear_least_squares_truth/' + file)
        )
