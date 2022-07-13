#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 12:38:00 2022

@author: macbookpro
"""

# https://www.youtube.com/watch?v=73r3KWiEvyk
# https://www.youtube.com/watch?v=rWAJCfYYOvM

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n=len(nums)
        return max(nums[0],self.helper(nums[0:n-1]),self.helper(nums[1:n]))
        
        
    def helper(self,nums):
        r1,r2=0,0
        
        for n in nums:
            temp=max(n+r1,r2)
            r1=r2
            r2=temp
        
        return r2
        
sol1 = Solution()
output = sol1.rob([3,1,4,14,7,2])

print (output)