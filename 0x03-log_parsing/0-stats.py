#!/usr/bin/python3
"""This script will deal with output of stats"""
import sys

line_counter = 0
file_counter = 0
dic = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        line_counter += 1
        sub = line.split(" ")
        get = sub[4].split('"')[1]
        two_60 = sub[5].split("/")[2]
        http = sub[6].split("/")[0]
        if (sub[1] == "-") and (get == "GET") and \
           (two_60 == "260") and (http == "HTTP") and \
           (sub[7] in dic.keys()):
            status = sub[7]
            if status in dic.keys():
                dic[status] += 1
            file_size = sub[8]
            file_counter += int(file_size)
            if (line_counter % 10 == 0):
                print("File size: {}".format(file_counter))
                for key, value in dic.items():
                    if (value != 0):
                        print("{}: {}".format(key, value))
        else:
            continue
except KeyboardInterrupt:
    print("File size: {}".format(file_counter))
    for key, value in dic.items():
        if (value != 0):
            print("{}: {}".format(key, value))
