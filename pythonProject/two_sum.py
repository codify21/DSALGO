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
# z1,z2=sum.twoSum([2,5,7,9],11)
z1,z2=sum.twoSum([3,2,4],6)

print(z1,z2)


# left = 0
# right = len(numbers) - 1
#
# while left < right:
#     value = numbers[left] + numbers[right]
#     if value == target:
#         return [left + 1, right + 1]
#     if value < target:
#         left += 1
#     else:
#         right -= 1