#!/usr/bin/python3
"""This script will find the minimum copy and paste"""


def minOperations(n):
    """This function will find the minimum copy and paste"""
    H = 1
    carry = 0
    cp = 0
    while (H < n):
        rest = n - H
        if (rest % H == 0):
            carry = H
            H += carry
            cp += 2
        else:
            H += carry
            cp += 1
    return cp
