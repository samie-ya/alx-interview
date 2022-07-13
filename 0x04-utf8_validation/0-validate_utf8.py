#!/usr/bin/python3
"""This script will check utf-8 validity"""


def validUTF8(data):
    """This script will return true if given list is a valid UTF-8"""
    num_bytes = 0
    bits = format(data[0], '#010b')[-8:]
    for bit in bits:
        if bit == '0':
            break
        else:
            num_bytes += 1
    if num_bytes == 1 or num_bytes > 4:
        return False
    return True
