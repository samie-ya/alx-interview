#!/usr/bin/python3
"""This script will check utf-8 validity"""


def validUTF8(data):
    """This script will return true if given list is a valid UTF-8"""
    num_byte = 0
    bits = format(data[0], '08b')
    if len(bits) == 8:
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
                if len(bits) == 8:
                    if (bits[0] != '1' and bits[1] != '0'):
                        return False
                return False
        elif (num_byte >= 5 or num_byte == 1):
            return False
        return True
    return False
