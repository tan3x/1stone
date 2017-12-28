#!/bin/python

import sys
import random
import numpy


'''

n = int(raw_input('Enter number of array element: ').strip())
arr = map(int,raw_input('Array elements: ').strip().split(' '))
print 'Reversed order:',
for i in reversed(arr):
    print  i,


def solve(a0, a1, a2, b0, b1, b2):

    A = sum([(1 if a0 > b0 else 0), (1 if a1 > b1 else 0), (1 if a2 > b2 else 0)])
    B = sum([(1 if b0 > a0 else 0), (1 if b1 > a1 else 0), (1 if b2 > a2 else 0)])

    return A, B


a0, a1, a2 = raw_input("\nAlice values: ").strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input("\nBob values: ").strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]

result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))

'''

# iUp, jUp = 6,6
# matrix = [[random.randint(0,9) for i in xrange(iUp)] for j in xrange(jUp)]

a = []
sum_list = []
for row in xrange(6):
    row = []
    for column in xrange(6):
        row.append(random.randint(1,10))
        a.append(row)

def glassWatch(arr):

    for x in xrange(1,5):

        for y in xrange(1,5):

            sumTemp = sum(arr[x-1][y-1:y+2]+ [arr[x][y]]+arr[x+1][y-1:y+2])
            sum_list.append(sumTemp)

    return max(sum_list)


print "res", glassWatch(a)








