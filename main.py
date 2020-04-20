"""
A program that approximates CPU Tempteratures using piecewise linear
interpolation and linear least squares.

by Jay Speidell for CS 417.

For more details, see README.md

To run the program, use the command:
> python main.py filename includes_units

Where includes_units is a yes/no statement describing the input file.

"""
import sys
from solver import solve
from numpy import array, append
import linear_piecewise_interpolation
from parse_temps import (parse_raw_temps)


__all__ = ['main']

def main():
    """
    main()


    """
    input_temps = sys.argv[1]
    includes_units = sys.argv[2] == "yes"

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


    linear_piecewise_interpolation.piecewise_solver(index, data)




if __name__== "__main__":
  main()
