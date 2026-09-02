#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:20:17 2021

@author: macbookpro
"""
# https://leetcode.com/problems/3sum-closest/
from typing import List
import time
start = time.time()

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0]+nums[1]+nums[-1]
        nums.sort()
        # triplets=[]
        for i in range(len(nums)-2):
            low=i+1
            high= len(nums) - 1
            
            while(low<high):
                current_sum = nums[i]+nums[low]+nums[high]
                if current_sum<target:
                    low=low+1
                else:
                    high= high -1
                if abs(current_sum-target)<abs(result-target):
                    result=current_sum
        #             triplets.append([nums[i],nums[low],nums[high]])#not correct
        # return triplets[-1]
        return result
                    


s = Solution()
threeSum = s.threeSumClosest([0,2,1,-3],1)
# threeSum = s.threeSumClosest([0,2,1,2,5,1,7,8,3,5,7,8,-2,-3,-1],5)
print(threeSum)
end = time.time()
print(end - start)