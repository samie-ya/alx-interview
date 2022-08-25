#!/usr/bin/python3
"""This script will create a prime game"""

def findPrimes(number):
    """This function will find a list of prime numbers until number"""
    primes = []
    for num in range(number + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i == 0):
                    break
            else:
                primes.append(num)
    return primes


def isWinner(x, nums):
    """This function will let Maria and Ben play"""
    Maria = 0
    Ben = 0
    for number in nums:
        maria = 0
        ben = 0
        if (number == 1):
            ben += 1
        else:
            for num in range(number + 1):
                if num > 1:
                    for i in range(2, num):
                        if (num % i == 0):
                            break
                    else:
                        if maria == ben:
                            maria += 1
                        elif maria > ben:
                            ben += 1
                        else:

                    
