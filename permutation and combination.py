#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 02:42:18 2022

@author: macbookpro
"""
import copy
from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        return permutations(nums) #one liner
        
        res=[]
        
        def backtrack(start ,comb):
            if len(comb)==len(nums):
                res.append(comb.copy())
                return
            
            for i in range(len(start)):
                temp=copy.deepcopy(start)
                comb.append(start[i])
                temp.remove(start[i])
                backtrack(temp,comb)
                comb.pop()
        
        backtrack(nums,[])
        return res

        
sol1 = Solution()
output = sol1.permute([1,2,3,4,5,6,7,8,9,10,11,12])
for i in output:
    print(i)