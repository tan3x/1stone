#!/bin/python

import sys
import random
import numpy


#
#
# n = int(raw_input('Enter number of array element: ').strip())
# arr = map(int,raw_input('Array elements: ').strip().split(' '))
# print 'Reversed order:',
# for i in reversed(arr):
#     print  i,
#
#
# def solve(a0, a1, a2, b0, b1, b2):
#
#     A = sum([(1 if a0 > b0 else 0), (1 if a1 > b1 else 0), (1 if a2 > b2 else 0)])
#     B = sum([(1 if b0 > a0 else 0), (1 if b1 > a1 else 0), (1 if b2 > a2 else 0)])
#
#     return A, B
#
#
# a0, a1, a2 = raw_input("\nAlice values: ").strip().split(' ')
# a0, a1, a2 = [int(a0), int(a1), int(a2)]
# b0, b1, b2 = raw_input("\nBob values: ").strip().split(' ')
# b0, b1, b2 = [int(b0), int(b1), int(b2)]
#
# result = solve(a0, a1, a2, b0, b1, b2)
# print " ".join(map(str, result))
#
#
#
# # iUp, jUp = 6,6
# # matrix = [[random.randint(0,9) for i in xrange(iUp)] for j in xrange(jUp)]
#
# a = []
# sum_list = []
# for row in xrange(6):
#     row = []
#     for column in xrange(6):
#         row.append(random.randint(1,10))
#         a.append(row)
#
# def glassWatch(arr):
#
#     for x in xrange(1,5):
#
#         for y in xrange(1,5):
#
#             sumTemp = sum(arr[x-1][y-1:y+2]+ [arr[x][y]]+arr[x+1][y-1:y+2])
#             sum_list.append(sumTemp)
#
#     return max(sum_list)
#
#
# class Person:
#     def __init__(self, initialAge):
#         # Add some more code to run some checks on initialAge
#         self.age = 0
#         self.initialAge = initialAge
#         if initialAge < 0:
#             print ('Age is not valid, setting age to 0.')
#         else:
#             initialAge = self.age
#
#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self.initialAge < 13:
#             print ('You are young.')
#         elif 13 <= self.initialAge < 18:
#             print ('You are a teenager.')
#         else:
#             print ('You are old.')
#
#     def yearPasses(self):
#         # Increment the age of the person in here
#         self.initialAge += 1
#
# from functools import reduce
#
# def aVeryBigSum(n, ar):
#     return reduce(lambda x, y: x + y, ar, 0)
#
# def reduce(func, arr, s):
#     for v in arr:
#         s = func(s, v)
#     return s
#
#
# d1, d2  = 0 , 0
# n = int(raw_input().strip())
# a = []
# for i in range(n):
#     a_temp = map(int,raw_input().strip().split(' '))
#
#     d1 += int(a_temp[i])
#     d2 += int(a_temp[n-i-1])
#     result = abs(d1-d2)
# print result
#
#
#
# n2 = float(raw_input().strip())
# arr2 = [int(x) for x in raw_input().split()]
#
# print round(len([x for x in arr2 if x>0])/n2,3)
# print round(len([x for x in arr2 if x<0])/n2,3)
# print round(len([x for x in arr2 if x==0])/n2,3)
#
#
#
# n = int(raw_input("n: "))
# for i in xrange(n):
#     print (" "*(n-i-1)+"#"*(i+1))
#
#
#
#
# #ele_list = map(int, raw_input().strip().split(' '))
# ele_list = []
# sum_list = []
#
# for i in xrange(5):
#     ele_list.append(random.randint(1,5))
#     print "element list" , ele_list
#     sum_list.append(sum(ele_list) - ele_list[i])
#     print "sum list" , sum_list
# print min(sum_list), max(sum_list)



#
# arr = []
# n = int(raw_input().strip())
# ar = map(int, raw_input().strip().split(' '))
# for i in xrange(n):
#     arr.append(random.randint(1,55))
#
#
# print arr.count(max(arr))


# from time import strptime, strftime
# print strftime("%H:%M:%S", strptime(raw_input(), "%I:%M:%S%p"))

# t = int(raw_input().strip())

# for i in xrange(t):
#     s_list = raw_input().strip()
#     print s_list
#     print s_list[0::2] + ' ' + s_list[1::2]

#
#with open("./sil/test.txt") as f:
#     for line in f:
#         print line
#
# def solve(grade):
#
#     for i in grade:
#         if i >= 38:
#             if i % 5 > 2:
#                 i += 5 - i % 5
#         print i,
#
# n = int(raw_input('number of students:').strip())
#
# grades = []
# for i in xrange(n):
#     grades.append(int(raw_input().strip()))
#
# solve(grades)

# def printarg(*args):
#     print args
# alist = [1,2,3]
# printarg (alist)
#
# def shift(a, d):
#     return a[d:] + a[:d]
#
# if __name__ == "__main__":
#     n, d = raw_input().strip().split(' ')
#     n, d = [int(n), int(d)]
#     a = map(int, raw_input().strip().split(' '))
#     result = shift(a, d)
#     print " ".join(map(str, result))

# from collections import Counter, defaultdict
#
# counter = defaultdict(int, Counter([raw_input() for _ in range(input())]))
#
# for _ in range(input()):
#     print counter[raw_input()]


# reversed array
#print list(reversed(arr))
#print(" ".join(map(str, arr[::-1])))
# for i in reversed(arr):
#     print i,




















