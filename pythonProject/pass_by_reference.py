#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 15:15:40 2022

@author: macbookpro
"""

# Passing of values in Python: 
# https://realpython.com/python-pass-by-reference/
# 1. Function arguments initially refer to the same address as their 
# original variables.
# Reassigning the argument within the function gives it a new address 
# while the original variable remains unmodified.


# def abc(a):
#     a[0] = 10
#     print('a',id(a))

# def xyz(b):
#     b[0] = 10
#     print('b',id(b))
#     return b


# def calc():
#     c = [1, 2, 3]
#     d = [1, 2, 3] 
#     print('c',id(c))
#     print('d',id(d))

#     abc(c)
#     d = xyz(d)
#     print('d2',id(d))
 
#     print(c, d)

# calc()

def swap(a, b):
    a, b = b, a
    print('a',id(a))
    print('b',id(b))


a, b = [1], [0]
print('a global',id(a))
print(' b global',id(b))

swap(a, b)
print('a global',id(a))
print(' b global',id(b))
print(a, b)