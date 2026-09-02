#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 02:08:44 2021

@author: macbookpro
"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        loc=0
        for i in range(len(candidates)):
            if candidates[i] <= target:
                loc = i
                continue
            else:
                break
        # print(loc)
        low=0
        output = target
        combo=[]
       
        for i in range(loc,-1,-1):
            if output - candidates[i]>=0:
                output = output - candidates[i]
                combo.append(candidates[i])
        print(combo)
        
        
        
        
s= Solution()
print(s.combinationSum([1,2,3,4,8,10],6))