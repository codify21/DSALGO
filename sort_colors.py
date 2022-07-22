#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 04:04:42 2022

@author: macbookpro
"""



# https://www.youtube.com/watch?v=4xbWSRZHqac

from collections import Counter

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        
#         l,r = 0,len(nums)-1
#         i=0
        
#         def swap(i,j):
#             temp=nums[i]
#             nums[i]=nums[j]
#             nums[j]=temp
            
#         while i<=r:
#             if nums[i]==0:
#                 swap(l,i)
#                 l+=1
#             elif nums[i]==2:
#                 swap(r,i)
#                 r-=1
#                 i-=1# to nullify a special case where 0 might come in b/w your array
#             i+=1
        
        counter= Counter(nums)
        result = []
        start = 0 
        for i in range(3):
            end = start+counter[i]
            for j in range(start, end):
                nums[j] = i 
            start = end
        
        print(nums)
            
        

    
sol1 = Solution()
output = sol1.sortColors([2,0,2,1,1,0])
        
        