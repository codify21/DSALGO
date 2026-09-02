#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:28:08 2022

@author: macbookpro
"""
# https://leetcode.com/problems/subarray-sum-equals-k/ 
# https://www.youtube.com/watch?v=fFVZt-6sgyo
from typing import List

class Solution:  
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        curSum =0
        prefixSum = {0:1}
        
        for n in nums:
            curSum+=n
            diff = curSum-k
            
            res+=prefixSum.get(diff,0)
            prefixSum[curSum] = 1+prefixSum.get(curSum,0)
        
        return res

            
 
sol1 = Solution()
output = sol1.subarraySum([1,-1,1,1,1,1,1,1],3)

print (output)