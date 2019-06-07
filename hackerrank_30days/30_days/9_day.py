'''
https://www.hackerrank.com/challenges/30-recursion/problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return n
    else:
        return(n*factorial(n-1))


if __name__ == '__main__':
    n = 3
    print(factorial(n))
