#!/usr/bin/python3
"""This script will do back tracking using N Queens"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
else:
    try:
        n = int(sys.argv[1])
        if type(n) is int:
            if n < 4:
                print("N must be at least 4")
                exit(1)
            else:
                print("N is right")
    except ValueError as e:
        print("N must be a number")
        exit(1)
