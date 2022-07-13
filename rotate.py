#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:49:15 2021

@author: macbookpro
"""

# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution:
     def rotate(self, nums,k):
         k=k%len(nums)        
         var = nums[-k:]
         print(var)
         if k==0:
             print (nums)
         else:
             for j in range(len(nums)-k-1,-1,-1):
                 swap(nums,j,j+k)
             nums[0:k]=var
             print(nums)

def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp
    
sol1 = Solution()
nums= [1,2,3,4,5,6,7]
output = sol1.rotate(nums,16)