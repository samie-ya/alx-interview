#!/usr/bin/python3
"""This script will calculate an island perimeter"""


def island_perimeter(grid):
    """This function will return the perimeter of the island"""
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if ((j - 1) >= 0) or ((j + 1) <= len(grid[i])):
                    try:
                        if grid[i][j - 1] == 0:
                            counter += 1
                    except IndexError as err:
                        counter += 1
                    try:
                        if grid[i][j + 1] == 0:
                            counter += 1
                    except IndexError as err:
                        counter += 1
                if ((i - 1) >= 0) or ((i + 1) <= len(grid)):
                    try:
                        if grid[i - 1][j] == 0:
                            counter += 1
                    except IndexError as err:
                        counter += 1
                    try:
                        if grid[i + 1][j] == 0:
                            counter += 1
                    except IndexError as err:
                        counter += 1
    return counter
