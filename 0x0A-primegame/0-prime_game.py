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
    for num in nums:
        maria = 0
        ben = 0
        allNum = []
        primeList = findPrimes(num)
        for i in range(1, num + 1):
            allNum.append(i)
        if (primeList == []):
            ben += 1
        else:
            for j in primeList:
                if (maria == ben):
                    maria += 1
                elif (maria > ben):
                    ben += 1
                else:
                    ben += 1
                for i in allNum:
                    if (i % j == 0):
                        allNum.remove(i)
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
