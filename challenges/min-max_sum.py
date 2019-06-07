'''
https://www.hackerrank.com/challenges/mini-max-sum/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # arr.sort()

    # min = sum(arr[:4])
    # max = sum(arr[len(arr)-4:])

    # print(min, max)

    minArr = []
    maxArr = []

    for num in arr:

        if len(minArr) < 4:
            minArr.append(num)
            maxArr.append(num)
            continue

        maxInMin = max(i for i in minArr)

        if maxInMin > num:
            minArr.remove(maxInMin)
            minArr.append(num)
        
        minInMax = min(i for i in maxArr)

        if minInMax < num:
            maxArr.remove(minInMax)
            maxArr.append(num)
            
    print(sum(minArr), sum(maxArr))

if __name__ == '__main__':
    arr=[7, 69, 2, 221, 8974]

    print(miniMaxSum(arr))