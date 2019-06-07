'''
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jumps = 0

    nextcloud = 1
    nextnextcloud = 2
    while nextcloud < len(c):

        if c[nextcloud] == 1:
            nextcloud += 2
            nextnextcloud += 2
            jumps += 1
            print('thundercloud')
            continue

        elif len(c) - nextcloud == 1:
            nextcloud += 1
            nextnextcloud += 1
            jumps +=1
            print('last cloud')
            continue
        
        elif c[nextnextcloud] == 0:
            nextcloud += 2
            nextnextcloud += 2
            jumps += 1
            print('2 cloud')
            continue

        else:
            nextcloud += 1
            nextnextcloud += 1
            jumps +=1
            print('1 cloud')
            

    return jumps



if __name__ == '__main__':

    c = [0, 0, 0, 1, 0, 0]

    print(jumpingOnClouds(c))

'''
https://stackoverflow.com/questions/1798796/python-list-index-out-of-range-error

'''