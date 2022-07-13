#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 04:25:36 2021

@author: macbookpro
"""
from typing import List

class Solution:
     def letterCombinations(self, digits: str) -> List[str]:
         
         combo= {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv',
                 '9':'wxyz'}
         char_dict={}
         
         digits = list(map(str,digits))  #'23'--  ['2', '3']  or  list(combo[digits[0]])
         print(combo[digits[0]])
         for i in range(len(digits)):
             characters = list(map(str,combo[digits[i]])) #['a', 'b', 'c']
             char_dict.update({digits[i]:characters}) #{'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}
         # print(char_dict)
         
         
         
          
         
sol = Solution()
sol.letterCombinations('234')
# print(list(map(ord,'a')))
