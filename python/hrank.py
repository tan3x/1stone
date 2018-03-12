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
#
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
#     print max(sum_list)
#     return max(sum_list)
#
# glassWatch(a)

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


# #number of entries in phonebook
# n = int(input().split())
# phoneBook = {}
#
# #assign in phoneBook
# for i in range(n):
#     name, num = input().strip().split(' ')
#     phoneBook[name] = num
#
# #query phoneBook while there is input, exit when EOF
# while(True):
#     try:
#         qName = input().strip()
#         if qName in phoneBook:
#             print('{}={}'.format(qName, phoneBook[qName]))
#         else:
#             print('Not found')
#     except EOFError:
#         break


# dictionary comprehension

# import sys
# n = input()
# name_numbers = [raw_input().split() for _ in range(n)]
# phone_book = {k: v for k,v in name_numbers}
# ls = map(lambda x: x.strip(),sys.stdin.readlines())
# for name in ls:
#     if name in phone_book:
#         print('%s=%s' % (name, phone_book[name]))
#     else:
#         print('Not found')


# recursive factorial

# def factorial(n):
#     # Complete this function
#     result = 1
#     if n <1:
#         return 1
#     else:
#         return (n * factorial(n-1))
#
# if __name__ == "__main__":
#     n = int(raw_input().strip())
#     result = factorial(n)
#     print result
#
# factorial(3)


# binary converter
#
# n1 = int(raw_input().strip())
#
# n1_b = "{0:b}".format(n1)
# cnt = 0
# for _ in n1_b:
#     if _ == '1':
#         cnt = cnt + 1
#
# print len(max(n1_b.split('0')))

#!/bin/python

# HourGlass 2
#
# arr = []
# arr_temp = []
# for arr_i in xrange(6):
#
#     arr_temp.append(random.randint(1,10))
#     #arr_temp = map(int,raw_input().strip().split(' '))
#     arr.append(arr_temp)
#
# res = []
#
# for x in range(0, 4):
#     for y in range(0, 4):
#         s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
#         res.append(s)
#
# print(max(res))


#
# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#
#     def printPerson(self):
#         print "Name:", self.lastName + "," + self.firstName
#         print "ID:", self.idNumber
#
# class Student(Person):
#
#         # Class Constructor
#     def __init__(self, firstName, lastName, idNumber, scores):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#         self.scores = scores
#
#     def calculate(self):
#         a=sum(self.scores)/len(self.scores)
#         if a >= 90:
#             return 'O'
#         elif 90>a>=80:
#             return 'E'
#         elif 80>a>=70:
#             return 'A'
#         elif 70>a>=55:
#             return 'P'
#         elif 55>a>=40:
#             return 'D'
#         else:
#             return 'T'
#
# line = raw_input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(raw_input())  # not needed for Python
# scores = map(int, raw_input().split())
# s = Student(firstName, lastName, idNum,scores)
# s.printPerson()
# print "Grade: " , s.calculate()

#Day 13
# from abc import ABCMeta, abstractmethod
# class Book:
#     __metaclass__ = ABCMeta
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display():
#         pass
#
# class MyBook(Book):
#     def __init__(self,title, author, price ):
#         self.title = title
#         self.author = author
#         self.price = price
#     def display(self):
#         print'Title: ' , title
#         print'Author: ', author
#         print'Price: ', price
#
# title = raw_input()
# author = raw_input()
# price = int(raw_input())
# new_novel = MyBook(title, author, price)
# new_novel.display()

#Day 14
# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#
#     def computeDifference(self):
#         '''
#         gets the maximum difference between any 2 array elements
#         :return:
#         '''
#
#         #self.maximumDifference = max(a) - min(a)
#         maximum = 0
#         for i in range(len(self.__elements)):
#             for j in range(len(self.__elements)):
#                 absolute = abs(self.__elements[i] - self.__elements[j])
#                 if absolute > maximum:
#                     maximum = absolute
#
#         self.maximumDifference = maximum
#
# _ = raw_input()
# a = [int(e) for e in raw_input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print d.maximumDifference

#linked list https://www.youtube.com/watch?v=njTh_OwMljA

# class Node:
#     def __init__(self,data):
#         self.data = data #contains data
#         self.next = None #contains the reference to the next node
#
# class Solution:
#     def display(self,head):
#         current = head
#         while current:
#             print current.data,
#             current = current.next
#
#     def insert(self, head, data):
#         if head is None:
#             head = Node(data)
#             self.tail = head
#         else:
#             node = Node(data)
#             self.tail.next = node
#             self.tail = node
#         return head
#
# mylist= Solution()
# T=int(input())
# head=None
# for i in range(T):
#     data=int(input())
#     head=mylist.insert(head,data)
# mylist.display(head);
# #
# S = raw_input().strip()
#
# try:
#     print int(S)
#
# except ValueError:
#     print "Bad String"


#exception
#
# class Calculator:
#     def power(self, n, p):
#         if n < 0 or p < 0:
#             raise Exception("n and p should be non-negative")
#         return pow(n, p)
#
#
# myCalculator = Calculator()
#
# T = int(raw_input())
# for i in range(T):
#     n, p = map(int, raw_input().split())
#     try:
#         ans = myCalculator.power(n, p)
#         print ans
#     except Exception, e:
#         print e


