"""
Contains a driver function to demonstrate that prepares the input for solving
a system of linear equations, uses the rref() function in rref.py to solve it,
then returns the results.
"""

from numpy import array, concatenate, zeros
from multiply import multiply
from rref import rref

__all__ = ['solve']

def solve(X, Y, PrintZero=True, Verbose=False):
    """
    A driver function that builds the system of linear equations, calls rref()
    to solve it, and then returns the solution in string form. It also has
    the option of printing all intermediate steps, and that is why it is so
    big.

    Parameters
    -------
    X : numpy.array X
    Xt : numpy.array the transpose of X
    Y : numpy.array Y
    PrintZero : boolean
        Whether or not to print zero coefficients, in string return, default is True
    Verbose : boolean
        whether or not to print all steps, default is False

    Returns
    -------
    - _ : list
        list of coefficients
    - phi_hat : string
        the solution equation as a string.
    """
    Xt = transpose(X)

    XtX = multiply(Xt,X)
    XtY = multiply(Xt,Y)

    if Verbose:
        print()
        print("X:")
        print(X)
        print()
        print("Xt:")
        print(Xt)
        print()
        print("Y:")
        print(Y)
        print()
        print("XtX:")
        print(XtX)
        print()
        print("XtY:")
        print(XtY)
        print()


    try:
        system = concatenate((XtX, XtY), axis=1)
    except:
        # Concatenate can't broadcast 1d to 2d,
        # need to convert to 2d manually before broadcast. 
        system = concatenate((XtX, XtY[:,None]), axis=1)

    if Verbose:
        print("System of Linear Equations: ")
        print(system)
        print()

    solved = rref(system)

    if Verbose:
        print("Solution:")
        print(solved)
        print()

    phi_hat = "phi_hat = "
    for x, c in enumerate(solved[:,-1]):
        if (int(c) != 0 or PrintZero == True):
            phi_hat += str(c)
            if (x >= 1):
                phi_hat += " * x^" + str(x)
            if (c != len(solved[:,-1]) - 2):
                phi_hat += " + "

    return list(solved[:,-1]), phi_hat


def transpose(X):
    """
    A simple function to transpose a matrix.

    Parameters
    -------
    X : numpy.array X

    Returns
    -------
    Xt : numpy.array
        The transpose of X
    """
    if len(X.shape) == 1:
        return X
    else:
        Xt = zeros((X.shape[1], X.shape[0]))
        for i in range(X.shape[0]):
            for j in range(X.shape[1]):
                Xt[j][i] = X[i][j]

    print(Xt)

    return Xt
