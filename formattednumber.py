#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:59:47 2021

@author: macbookpro
"""
# def formatted(strArr):
    
#     strArr=strArr[0]
#     decimal=strArr.split('.')
#     if len(decimal)>2:
#         return False
#     number = decimal[:1]
#     number = number[0].split(',')
#     for i in range(1,len(number)):
#         if len(number[i])==3:
#             continue
#         else:
#             return False
#     if len(number[0]) in [1,2,3]:
#         return True
# strArr=["256,700.00034"]
# print(formatted(strArr))

def FormattedNumber(strArr):
  c=1

  strArr=strArr[0]
  decimal=strArr.split('.')
  if len(decimal)>2:
    print(0)
    return False
    
  number = decimal[:1]
  number = number[0].split(',')
  for i in range(1,len(number)):
    if len(number[i])==3:
      continue
    else:
      print(1)
      return False
  if len(number[0]) in[1,2,3]:
      c=1
      print(2)
      return True

# keep this function call here 
print (FormattedNumber(["1,093,222.04"]  ))
# if value==  
# print('true')
# else:
#   print('false')