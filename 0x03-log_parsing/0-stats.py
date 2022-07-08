#!/usr/bin/python3
"""This script will deal with output of stats"""
import sys
from datetime import datetime


def validate_ip(s):
    a = s.split(".")
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True


line_counter = 0
file_counter = 0
dic = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        line_counter += 1
        sub = line.split(" ")
        if (len(sub) == 9):
            combo = sub[2] + sub[3]
            combo_with_no_bracet = combo[1: -1]
            date = datetime.strptime(combo_with_no_bracet,
                                     "%Y-%m-%d%H:%M:%S.%f")
            method = sub[4] + " " + sub[5] + " " + sub[6]
            size = sub[8].split("\n")[0]
            if (validate_ip(sub[0])) and (sub[1] == "-") and \
               (isinstance(date, datetime)) and \
               (method == "\"GET /projects/260 HTTP/1.1\"") and \
               (sub[7] in dic.keys()) and size.isnumeric():
                status = sub[7]
                if status in dic.keys():
                    dic[status] += 1
                file_size = sub[8]
                file_counter += int(file_size)
                if (line_counter % 10 == 0):
                    print("File size: {}".format(file_counter))
                    for key, value in sorted(dic.items()):
                        if (value != 0):
                            print("{}: {}".format(key, value))
            else:
                continue
        else:
            continue
except KeyboardInterrupt:
    print("File size: {}".format(file_counter))
    for key, value in sorted(dic.items()):
        if (value != 0):
            print("{}: {}".format(key, value))
else:
    print("File size: {}".format(file_counter))
    for key, value in sorted(dic.items()):
        if (value != 0):
            print("{}: {}".format(key, value))
