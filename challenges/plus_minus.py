'''
https://www.hackerrank.com/challenges/plus-minus/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count = {}
    count['pos'] = count['neg'] = count['zero'] = 0

    for num in arr:
        if num > 0:
            count['pos'] += 1
        elif num < 0:
            count['neg'] += 1
        else:
            count['zero'] += 1
            
    for k, v in count.items():
        print(v/len(arr))

if __name__ == '__main__':
    n = [-4, 3, -9, 0, 4, 1]

    plusMinus(n)