'''
https://www.hackerrank.com/challenges/30-review-loop/problem?h_r=next-challenge&h_v=zen
'''

#!/usr/bin/env python3

if __name__ == "__main__":
    # n = int(input())
    for i in range(int(input())):
        string = input()
        # for i in range(len(string)):
        print(string[::2], string[1::2])