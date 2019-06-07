'''
https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    tl_to_br = 0
    bl_to_tr = 0

    for i in range(len(arr[0])):
        tl_to_br += arr[i][i]

    count = len(arr)-1
    for i in range(len(arr)):
        while count >= 0:
            bl_to_tr += arr[count][i]
            count -= 1
            break

    return(abs(tl_to_br - bl_to_tr))

if __name__ == '__main__':

    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

    print(diagonalDifference(arr))
