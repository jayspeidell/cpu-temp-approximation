#! /usr/bin/env python3

"""
This module is a collection of input helpers for the CPU Temperatures Project.
All code may be used freely in the semester project, iff it is imported using
``import parse_temps`` or ``from parse_temps import {...}`` where ``{...}``
represents one or more functions.
"""


from typing import (TextIO, Iterator, List, Tuple)


def parse_raw_temps(original_temps: TextIO,
                    step_size: int = 30,
                    units: bool = True) -> Iterator[Tuple[float, List[float]]]:
    """
    Take an input file and time-step size and parse all core temps.

    Args:
        original_temps: an input file

        step_size: time-step in seconds

        units: True if the input file includes units and False if the file
               includes only raw readings (no units)

    Yields:
        A tuple containing the next time step and a List containing _n_ core
        temps as floating point values (where _n_ is the number of CPU cores)
    """

    if units:
        for step, line in enumerate(original_temps):
            yield (step * step_size), [float(entry[:-2]) for entry in line.split()]
    else:
        for step, line in enumerate(original_temps):
            yield (step * step_size), [float(entry) for entry in line.split()]
