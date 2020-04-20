import pytest


import os
import glob
import filecmp
from parse_temps import (parse_raw_temps)
from numpy import array, append, array_equal, allclose
