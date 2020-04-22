"""
A module for calculating linear least squares for parallel series
of time step data points and printing the subsequent formulas to individual
text files.

Depends on:

parse_temps.parse_raw_temps
sys
os.path
numpy

Constants
----------

BASE_FILENAME : start
    A base string for generating filenames
COL_WIDTH : int
    The default output column width when printing to text file.
PRECISION : int
    The precision of all floats in text output.
COL_1 : string
    An output template for column 1.
COL_2 : string
    An output template for column 2.
COL_3 : string
    An output template for column 3.
COL_4 : string
    An output template for column 4.
COL_5 : string
    An output template for column 5.
LINE : string
    A concatenation of all output templates for printing a full line.
"""

from .parse_temps import (parse_raw_temps)
import sys
from os import path
import numpy as np
from .solver import solve

BASE_FILENAME = "Linear_Least_Squares_Core_"

# Column formatting
COL_WIDTH = 10
PRECISION = 4

COL_1 = "| {0:>" + str(COL_WIDTH) + "} <= x < "
COL_2 = " {1:>" + str(COL_WIDTH) + "}; "
COL_3 = " y_{2:<" + str(COL_WIDTH) + "} ="
COL_4 = "{3:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f} + "
COL_5 = "{4:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f}x; approximation \n"

LINE = COL_1 + COL_2 + COL_3 + COL_4 + COL_5



def linear_least_squares(timestamps, data, output = 'output/'):
    """
    Use a matrix solver to find a generalized linear least squares solution
    that approximates the input data with a line. This is a simple driver
    function for the solver module.

    {start time} <= {end time} < ; y_{step number} = {offset} + {slope}x; approximation

    Parameters
    -------
    timestamps : list(int)
        A list of timestamps from the input file.
    data : numpy.array
        An array of temperature readings where rows represent time steps and
        columns represent CPU cores.
    output : string
        The base directory for output.

    Returns
    -------
    None
    """

    active_files = []
    for i in range(data.shape[1]):
        active_files.append(open(output + BASE_FILENAME + str(i+1) + ".txt", 'a+'))

    for i, file in enumerate(active_files):
        X = np.column_stack((np.ones(data.shape[0]), timestamps))
        Y = data[:,i]
        val, _ = solve(X,Y)
        file.write(LINE.format(min(timestamps), max(timestamps), 0,
                    val[0], val[1]))

    for file in active_files:
        file.close()
