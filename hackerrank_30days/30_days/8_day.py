'''
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

#!/usr/bin/env python3

if __name__ == '__main__':
    entries = int(input())
    phoneBook = {}
    for i in range(entries):
        entry = input().split(' ')
        phoneBook[entry[0]] = entry[1]

    while True:
        try:
            query = input()
            if query in phoneBook.keys():
                print(query + '=' + phoneBook[query])
            else:
                print('Not found')
        except EOFError:
            break