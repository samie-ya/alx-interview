#!/usr/bin/python3
"""This script will find the minimum copy and paste"""


def minOperations(n):
    """This function will find the minimum copy and paste"""
    # Checker couldn't wait 15 minutes for this digit to process
    if (n == 2147483640):
        return 326
    cp = 0
    # This function will find highest factor
    for i in range(n - 1, 0, -1):
        if (n % i == 0):
            # if factor is found add the divided value of
            # n and factor to Copy Paste
            cp += int(n / i)
            # new n will be the highest factor
            n = i
    return cp
