"""
A reduce row echelon form module for solving systems of linear equations.

No dependencies. I used a list conversion to avoid the numpy
import here.

The main driver function is rref(), other function support it.
"""

__all__ = ['rref', 'swap_rows', 'row_scale', 'eliminate', 'backsolve']

import numpy as np

def rref(arr):

    """
    A driver function to solve a linear system of equations
    to their reduced row echelon form.

    Parameters
    -------
    arr : numpy.array
        the system of linear equations to be solved

    Returns
    -------
    arr : numpy.array
        the rref
    """
    for col in range(arr.shape[1] - 1):
        for row in range(arr.shape[0]):
            idx = list(arr[:,col]).index(max(arr[:,col]))
            if (idx > col):
                arr = swap_rows(arr, row, idx)
            arr = row_scale(arr, row)
            arr = eliminate(arr, row)
    arr = backsolve(arr)
    return arr

def swap_rows(arr, row, idx):
    """
    A function that swaps two rows in a numpy array.

    Parameters
    -------
    arr : numpy.array
        the input array
    row : int
        the index of the row being examined by the top level function
    idx : int
        the intex of the row to be swapped with "row"

    Returns
    -------
    arr_new : numpy.array
        a copy of the input array with the rows swapped
    """
    arr_new = arr.copy()
    arr_new[row,:] = arr[idx,:]
    arr_new[idx,:] = arr[row,:]
    return arr_new

def row_scale(arr, row):
    """
    A function to scale one row of a numpy array based on the index being
    examined. It results in the original [row][row] value scaled to one
    and the rest of the row scaled accordingly.

    Parameters
    -------
    arr : numpy.array
        the input array
    row : int
        the index of both row and column being examined

    Returns
    -------
    arr : numpy.array
        the array with one row scaled
    """
    factor = arr[row,row]
    if (factor != 0):
        for col in range(arr.shape[1]):
            arr[row,col] = arr[row,col] / factor
    return arr

def eliminate(arr, target_row):
    """
    A function to change all values of the target column, apart from
    the target row, to zero. The rest of the row is modified accordingly
    as the whole rows are subtracted from each other.

    Parameters
    -------
    arr : numpy.array
        the input array
    row : int
        the index of both the row and column being examined

    Returns
    -------
    arr : numpy.array
        the array with appropriate values eliminated
    """
    target_col = target_row
    for row in range(target_row + 1, arr.shape[0]):
        factor = arr[row,target_col]
        for col in range(target_col, arr.shape[1]):
            arr[row,col] = arr[row,col] - factor * arr[target_row,col]
    return arr

def backsolve(arr):
    """
    A function to rake the row echelon form of a matrix and reduce it to the
    reduced row echelon form.

    Parameters
    -------
    arr : numpy.array
        an array in ref

    Returns
    -------
    arr : numpy.array
        the input array in rref
    """

    last_row = arr.shape[0] - 1
    last_col = arr.shape[1] - 1

    for target_row in range(last_row,-1,-1):
        for elim_row in range(target_row-1,-1,-1):
            if (target_row == elim_row):
                pass
            factor = arr[elim_row][target_row]
            for col in range(target_row, last_col+1):
                arr[elim_row][col] -= float(factor * arr[target_row][col])

    return arr
