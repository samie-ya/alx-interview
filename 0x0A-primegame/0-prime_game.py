#!/usr/bin/python3
"""This script will create a prime game"""


def isWinner(x, nums):
    """This function will let Maria and Ben play"""
    Maria = 0
    Ben = 0
    for i in range(x):
        maria = 0
        ben = 0
        if (nums[i] == 1):
            ben += 1
        else:
            for num in range(nums[i] + 1):
                if num > 1:
                    for i in range(2, num):
                        if (num % i == 0):
                            break
                    else:
                        if maria == ben:
                            maria += 1
                        elif maria > ben:
                            ben += 1
        if (maria > ben):
            Maria += 1
        elif (ben > maria):
            Ben += 1
        else:
            Ben += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    else:
        return None
