#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 17:49:55 2021

@author: macbookpro
"""
#Recursive Approach
# class Solution:
#     def search(self, nums, target,start,end ):
#         if start<=end:
#             mid = (start+end)//2
            
#             if target<nums[mid]:
#                 return self.search(nums,target,start,mid-1)
#             elif target>nums[mid]:
#                 return self.search(nums,target,mid+1,end)
#             else:
#                 return mid
#         else:
#             return -1
        
        
        
# sol = Solution()
# nums= [-1,0,3,5,9,12]
# output = sol.search(nums,12,0,len(nums)-1)
# print(output)

#Iterative Approach 

class Solution1:
    def search(self, nums, target):
        
        low = 0 
        high = len(nums)-1
        mid = 0
        
        while low<=high:
            
            mid = (high+low)//2
            
            if target == nums[mid]:
                return mid               
            elif target>nums[mid]:
                low =mid+1
            else:
                 high = mid-1
                
            
        return -1
                

sol1 = Solution1()
nums= [-1,0,3,5,9,12]
output = sol1.search(nums,12)
print(output)
        
        
        