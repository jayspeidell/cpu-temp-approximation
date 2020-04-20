"""
A matrix multiplication module.

Depends on:

numpy.array
numpy.zeros
"""

from numpy import array, zeros

__all__ = ['multiply']

def multiply(lhs, rhs):
    """
    Multiply two matrices and return the result.

    Parameters
    -------
    lhs : numpy.array
        left hand matrix
    rhs : numpy.array
        Right hand matrix

    Returns
    -------
    result : numpy.array
        The resulting matrix
    """
    result = zeros((lhs.shape[0], rhs.shape[1]))

    for i in range(lhs.shape[0]):
        for j in range(rhs.shape[1]):
            for k in range(lhs.shape[1]):
                result[i][j] += lhs[i][k] * rhs[k][j]

    return result
