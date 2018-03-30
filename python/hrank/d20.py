#!/bin/python

import sys

# n = int(raw_input().strip())
# a = map(int, raw_input().strip().split(' '))

n = 3
a=[2,1,3]
numSwaps = 0 
firstElement = a[0];
lastElement = a[-1];
i=0;

def swap0(s1, s2):
    assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    s1[:] = s2
    s2[:] = tmp



count=0
n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))

for i in xrange(n):
    j=0
    while j<n-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            count+=1
        j+=1
print 'Array is sorted in %d swaps.'%count
print 'First Element: %d'%a[0]
print 'Last Element: %d'%a[-1]


