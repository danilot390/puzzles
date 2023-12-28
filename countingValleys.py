import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Initialize varibles
    cont = 0
    level = 0
    into = False
    # Following steps
    for step in path:
        if step == 'U':
            level += 1
        else:
            level -= 1
        # Into the valley   
        if level == -1:
            into = True
        # Onto and count the valley
        if into and level == 0:
            cont += 1
            into = False
    # Return enters and leaves the valley
    return int(cont)
if __name__ == '__main__':
    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(result)
