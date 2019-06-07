'''
https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    for i in range(1,n+1):
        print((' '*(n-i)) + ('#'*i))
    
if __name__ == '__main__':
    staircase(8)