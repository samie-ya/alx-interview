#!/usr/bin/python3
"""This script will unlock list of list"""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """
    tests = set()
    lists = set()
    # Add all values of boxes whether they are keys or not
    for i in range(len(boxes)):
        for key in boxes[i]:
            tests.add(key)
    # Adds into set the first list, which is unlocked
    for key in boxes[0]:
        lists.add(key)
    # Checks if the value of list of list is in the key container
    # 'lists'
    for i in range(len(boxes)):
        for key in boxes[i]:
            if (key in lists):
                # If key is in the collection of keys then open
                # the list of list box and add contents into 'lists'
                for value in boxes[key]:
                    lists.add(value)
    # If all the key in 'lists' aren't in test return False
    if (tests != lists):
        return False
    return True
