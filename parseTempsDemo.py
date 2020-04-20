#! /usr/bin/env python3

import sys

from parse_temps import (parse_raw_temps)


def main():
    """
    This main function serves as the driver for the demo. Such functions
    are not required in Python. However, we want to prevent unnecessary module
    level (i.e., global) variables.
    """

    input_temps = sys.argv[1]
    includes_units = sys.argv[2] == "yes"  # set to False for files without units

    print(includes_units)

    with open(input_temps, 'r') as temps_file:
        for temps_as_floats in parse_raw_temps(temps_file, units=includes_units):
            print(temps_as_floats)


if __name__ == "__main__":

    main()
