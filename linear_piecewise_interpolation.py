"""
A module for calculating piecewise linear interpolation for parallel series
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
    """
    A Step represents one piecewise step in linear interpolation. An instance
    is initialized with `start`, `data`, and `stepno` and uses information from
    the following Step instance in the sequence to update `end` and `slope`.

    The class scales to handle parallel timelines.

    Attributes
    ----------
    start : int
        The starting time stamp for this piecewise segment.
    end : int
        The end time stamp for this piecewise segment.
    data : list of floats
        A list of starting x values for line segments associated with this
        time step.
    stepno : int
        The sequence number of this segment.
    slope : list of floats
        A list of slope values for line segments associated with this time step.

    Methods
    -------
    __init__(self, start=-1, end=-1, data=[], stepno=-1, slope=[])
        The constructor for this class containing default values for every
        attribute.

    process(self, next_step)
        A method that updates the current step with information from the next
        step.
    """
    def __init__(self, start=-1, end=-1, data=[], stepno=-1, slope=[]):
        """
        The constructor for this class containing default values for every
        attribute.

        Parameters
        ----------
        start : int
            The starting time stamp for this piecewise segment.
        end : int
            The end time stamp for this piecewise segment.
        data : list of floats
            A list of starting x values for line segments associated with this
            time step.
        stepno : int
            The sequence number of this segment.
        slope : list of floats
            A list of slope values for line segments associated with this time step.

        Returns
        -------
        None
        """
        self.start = start
        self.end = end
        self.data = data
        self.stepno = stepno
        self.slope = slope
    def process(self, next_step):
        """
        A method that updates the current step with information from the next
        step.

        Parameters
        ----------
        next_step : Step
            A Step instance containing information about the next step in the
            timeline. `next_step` contains `start`, `data`, and `stepno`
            information only.

        Returns
        -------
        None

        """
        self.slope = []
        self.end = next_step.start
        for i in range(len(self.data)):
            self.slope.append(
                                (next_step.data[i] - self.data[i]) /
                                (self.end - self.start)
                            )

def piecewise_solver(timestamps, data, output = 'output/'):
    """
    Iterate through a list of data points and print the resulting piecewise
    functions to a text file. One text file will be generated for each CPU
    for and each line will represent one piecewise step in the format:

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
