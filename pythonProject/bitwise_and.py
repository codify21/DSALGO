#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 02:11:53 2022

@author: macbookpro
"""
# https://leetcode.com/problems/bitwise-and-of-numbers-range/
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
         
           
        # if left==right:
        #     return left
        # if len(bin(left))==len(bin(right)) and left!=0:
        #     j=left
        #     for i in range(j+1,right+1):
        #         j&=i
        #         if j==0:
        #             return 0
        #     return(j)
        # return 0
          
           count=0
           while(left<right) and left!=0:
             left = left>>1
             right = right>>1
             count+=1
           return left<<count

        
sol1 = Solution()
output = sol1.rangeBitwiseAnd(1,5)
