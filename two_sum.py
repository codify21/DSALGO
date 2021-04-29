#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 03:53:12 2021

@author: macbookpro
"""
# https://leetcode.com/problems/two-sum
# to get two index of those numbers from list which will give output after summing both numbers
from typing import List

class Solution:
    def twoSum(self ,nums: List[int], target: int) -> List[int]:
        
        mydict = {}
        
        for i,num in enumerate(nums):
            print(str(i) + ' ' +str(num))
            complement = target - num
            if complement in mydict:
                return [mydict[complement], i]
            else:
                mydict[num] = i
                
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     a=[]
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]+nums[j]==target:
    #                 a.append(i)
    #                 a.append(j)
                    
    #                 return a
                
sum = Solution()
z=sum.twoSum([2,5,7,9],11)
print(z)