#!/usr/bin/python3
"""
 Calculates the fewest number of operations needed to result in
 exactly n H characters in the file.

Returns an integer
If n is impossible to achieve, return 0
"""


def minOperations(n):
    """
    returns the fewest number of operation needed to
    result exactly n number of H characters in the file
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
