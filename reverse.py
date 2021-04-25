#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 19:41:38 2021

@author: macbookpro
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x>2**31 or x <-(2**31):
            return 0
        x =str(x)
        sign = '0'#null flag value
        
        if x[0]== '-':
            sign = '-'
            x = abs(int(x))
        else:
            x = abs(int(x))
        num = 0
        while(x>0):
            r = x%10
            x = int(x/10)
            num = num*10 + r
        if sign == '-':
            num =str(num)
            num = '-'+num
            num = int(num)
        if num> (2**31 - 1) or num <-(2**31):
            return 0
        else:   
            return num
        
        
    # def reverse(self, x: int) -> int:
    #     if x>0:
    #         s = str(x)[::-1]
            
    #     else:
    #         x = -1*x
    #         s = '-'+str(x)[::-1]
        
    #     a = int(s)
    #     minn = -2**31
    #     maxx = 2**31 - 1
    #     if a in range(minn,maxx):
    #         return a
    #     else:
    #         return 0
        
    

s = Solution()
reverse = s.reverse(-1234)
print(reverse)
    