#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 03:53:12 2021

@author: macbookpro
"""
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
                
sum = Solution()
z=sum.twoSum([2,5,7,9],11)
print(z)