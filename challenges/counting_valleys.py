#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    position = 0

    valleys = 0
    
    for step in s:
        if step == 'U':
            position += 1
            if position == 0:
                valleys += 1
        
        if step == 'D':
            position -= 1
    
    return valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
