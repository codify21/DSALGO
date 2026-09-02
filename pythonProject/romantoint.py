#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:34:37 2021

@author: macbookpro
"""
# https://leetcode.com/problems/roman-to-integer/

# class Solution:
    # def romanToInt(self, s: str) -> int:
    #     answer = 0
    #     d = { 'I':[1 , 1 ], 'V':[2 , 5 ], 'X':[3 , 10], 'L':[4 , 50] ,\
    #         'C':[5, 100 ], 'D':[6, 500] , 'M':[7, 1000] }

    #     for i in range(len(s) -1):
    #         if d[s[i]][0]<d[s[i+1]][0]:
    #             answer += (-(d[s[i]][1]))
    #         else:answer += (d[s[i]][1])

    #     return answer+d[s[len(s)-1]][1]
    
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
            print(res)
        # print(res)
        res += d[s[len(s)-1]]
        return res
              
          
                 
        
s = Solution()
roman = s.romanToInt('MCMXCIV')
print(roman)