#!/usr/bin/python3
"""This script will unlock list of list"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """
    lists = [0]
    for i in range(len(boxes)):
        for key in boxes[i]:
            if (key not in lists and key != i):
                lists.append(key)
    if len(lists) == len(boxes):
        return True
    return False
