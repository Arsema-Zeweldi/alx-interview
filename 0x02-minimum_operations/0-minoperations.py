#!/usr/bin/python3
"""It calculates the fewest number of operations needed to result
in exactly n H characters in the file."""


def minOperations(n):
    H = 1
    copyPaste = 0
    noCopyPaste = 0
    while H < n:
        leftOver = n - H
        if (leftOver % H == 0):
            copyPaste = H
            H += copyPaste
            noCopyPaste += 2
        else:
            H += copyPaste
            noCopyPaste += 1
    return noCopyPaste
