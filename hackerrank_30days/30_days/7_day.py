'''
https://www.hackerrank.com/challenges/30-arrays/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    newArr = []
    for i in reversed(arr):
        newArr.append(str(i))
    print(' '.join(newArr))

