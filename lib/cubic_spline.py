"""
A module for calculating piecewise cubic spline functions for parallel series
of time step data points and printing the subsequent formulas to individual
text files.

This bonus module is not covered by unit tests, only pencil and paper.

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
COL_6 : string
    An output template for column 6.
COL_7 : string
    An output template for column 7.
LINE : string
    A concatenation of all output templates for printing a full line.
"""

from .parse_temps import (parse_raw_temps)
from .solver import solve
from .rref import rref
import sys
from os import path
import numpy as np

BASE_FILENAME = "Cubix_Spline_Core_"

# Column formatting
COL_WIDTH = 10
PRECISION = 4

COL_1 = "| {0:>" + str(COL_WIDTH) + "} <= x < "
COL_2 = " {1:>" + str(COL_WIDTH) + "}; "
COL_3 = " y_{2:<" + str(COL_WIDTH) + "} ="
COL_4 = "{3:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f} + "
COL_5 = "{4:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f}x "
COL_6 = "{5:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f}x^2 "
COL_7 = "{6:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f}x_3 ; Bezier Curve \n"

LINE = COL_1 + COL_2 + COL_3 + COL_4 + COL_5 + COL_6 + COL_7

def cubic_solver(timestamps, data, output = 'output/'):
    """
    Iterate through a list of data points and print the resulting piecewise
    functions (Bezier curves) to a text file. One text file will be generated
    for each CPU for and each line will represent one piecewise step in the
    format:

    {start time} <= {end time} < ; y_{step number} = {offset} + {slope}x; interpolation

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

    base = np.array([
        [2,1,0],
        [1,4,1],
        [0,1,2]
    ])

    count = 0
    for step in range(1,len(timestamps)-1,3):
        for core, file in enumerate(active_files):

            x_1 = timestamps[step-1]
            f_1 = data[step-1][core]

            x_2 = timestamps[step]
            f_2 = data[step][core]

            x_3 = timestamps[step+1]
            f_3 = data[step+1][core]

            dx_2 = x_2 - x_1
            dx_3 = x_3 - x_2

            f_1_2 = (f_2 - f_1) / dx_2
            f_2_3 = (f_3 - f_2) / dx_3

            b_1 = 3 * f_1_2
            b_2 = 3 * ( dx_2 * f_1_2 + dx_3 * f_2_3 )
            b_3 = 3 * f_2_3

            result = rref( np.concatenate( (base, np.array([
                                                                [b_1],
                                                                [b_2],
                                                                [b_3]
                                                            ])), axis=1))

            m_1 = result[0][3]
            m_2 = result[1][3]
            m_3 = result[2][3]

            file.write(LINE.format( timestamps[step-1],
                                    timestamps[step+1],
                                    count,
                                    f_1,
                                    m_1,
                                    m_2,
                                    m_3
                                    ))


        count += 1


            #file.write(LINE.format())

    for file in active_files:
        file.close()
