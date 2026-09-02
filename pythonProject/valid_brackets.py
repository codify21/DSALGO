#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 04:13:23 2021

@author: macbookpro
"""
# https://leetcode.com/problems/valid-parentheses/submissions/

class Solution:
     # def isValid(self, s):
     #    while "()" in s or "{}" in s or '[]' in s:
     #        s = s.replace("()", "").replace('{}', "").replace('[]', "")
     #    return s == ''
    
    
    def isValid(self, s: str) -> bool:
        parens = {'(': ')', '[': ']', '{': '}'}
        
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            
            elif(not stack):#  "[{}()]}()"--- IndexError: pop from empty list -[stack empty]
                return False
            else:
               d= parens[stack.pop()]
               if(c != d):
                    return False
                
        return len(stack) == 0
            
    
    # def isValid(self, s: str) -> bool:
    #     parens = {'(': ')', '[': ']', '{': '}'}
        
    #     stack = []
    #     for c in s:
    #         if c in parens:
    #             stack.append(c)
    #         elif not stack or parens[stack.pop()] != c:
    #             return False
                
    #     return len(stack) == 0
            
                
        

s = Solution()
reverse = s.isValid("[{}()]}()")
print(reverse)
    