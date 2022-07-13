#!/usr/bin/python3
"""This script will check utf-8 validity"""


def validUTF8(data):
    """This script will return true if given list is a valid UTF-8"""
    num_byte = 1
    bits = format(data[0], '08b')
    for bit in bits:
        if bit[0] == '0':
            break
        else:
            if bit != '0':
                num_byte += 1
            break
    if (num_byte > 1 and num_byte < 5):
        for i in range(1, num_byte):
            bits = format(data[i], '08b')
            if (bits[0] != '1' and bits[1] != '0'):
                return False
    return True
