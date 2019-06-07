'''
https://www.hackerrank.com/challenges/compare-the-triplets/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):

    a_b_score = [0,0]

    for i in range(len(a)):
        if a[i] > b[i]:
            a_b_score[0] += 1
        elif a[i] < b[i]:
            a_b_score[1] += 1
    
    return(a_b_score)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
