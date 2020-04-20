from parse_temps import (parse_raw_temps)
import sys
from os import path
import numpy as np

BASE_FILENAME = "Linear_Piecewise_Interpolation_Core_"

# Column formatting
COL_WIDTH = 10
PRECISION = 4

COL_1 = "| {0:>" + str(COL_WIDTH) + "} <= x < "
COL_2 = " {1:>" + str(COL_WIDTH) + "}; "
COL_3 = " y_{2:<" + str(COL_WIDTH) + "} ="
COL_4 = "{3:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f} + "
COL_5 = "{4:>" + str(COL_WIDTH) + "." + str(PRECISION) + "f}x; interpolation \n"

LINE = COL_1 + COL_2 + COL_3 + COL_4 + COL_5

class Step:
    def __init__(self, start=-1, end=-1, data=[], stepno=-1, slope=[]):
        self.start = start
        self.end = end
        self.data = data
        self.stepno = stepno
        self.slope = slope
    def process(self, next_step):
        self.slope = []
        self.end = next_step.start
        for i in range(len(self.data)):
            self.slope.append(
                                (next_step.data[i] - self.data[i]) /
                                (self.end - self.start)
                            )






def piecewise_solver(timestamps, data):
    """
    Iterate through a list of data points and print the resulting piecewise
    functions to a text file. One text file will be generated for each CPU
    for and each line will represent one piecewise step in the format:

    {start time} <= {end time} < ; y_{step number} = {offset} + {slope}x; interpolation

    This is a driver function and as such is not covered by unit tests, the real
    math is being done in the Step class.

    Parameters
    -------
    timestamps : list(int)
        A list of timestamps from the input file.
    data : numpy.array
        An array of temperature readings where rows represent time steps and
        columns represent CPU cores.

    Returns
    -------
    None
    """

    active_files = []
    for i in range(data.shape[1]):
        active_files.append(open(BASE_FILENAME + str(i+1) + ".txt", 'a+'))

    step = Step()
    next_step = Step()

    for index, time in enumerate(timestamps):
        if index == 0:
            step = Step(start=time, data=list(data[index]), stepno=index)
        else:
            next_step = Step(start=time, data=list(data[index]), stepno=index)
            step.process(next_step)
            for i, file in enumerate(active_files):
                file.write(LINE.format(step.start, step.end, step.stepno,
                            step.data[i], step.slope[i]))
            step = next_step

    for file in active_files:
        file.close()
