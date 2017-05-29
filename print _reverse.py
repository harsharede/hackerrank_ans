#Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
"""
Sample Input

4
1 4 3 2
Sample Output

2 3 4 1

"""


import sys

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

temp = ""

for i in range(len(arr)):
    temp = temp + str(arr[-1]) + " "
    arr.pop(-1)


print temp.strip()