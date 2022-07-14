#!/usr/bin/python3
"""This script will check utf-8 validity"""


def validUTF8(data):
    """This script will return true if given list is a valid UTF-8"""
    num_bytes = 0
    for i in range(len(data)):
        bits = format(data[i], '#010b')[-8:]
        if bits[0] == '0':
            continue
        else:
            for bit in bits:
                if bit != '0':
                    num_bytes += 1
                else:
                    break
            if num_bytes == 1 or num_bytes >= 5:
                return False
            if (num_bytes > 1 and num_bytes <= 4):
                after_byte = i + 1
                last_byte = i + num_bytes
                if (after_byte > len(data) or last_byte > len(data)):
                    return False
                for j in range(after_byte, last_byte):
                    new_bits = format(data[j], '#010b')[-8:]
                    if not (new_bits[0] == '1' and new_bits[1] == '0'):
                        return False
                    else:
                        continue
                return True
    return True
