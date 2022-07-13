#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:19:03 2021

@author: macbookpro
"""
# https://leetcode.com/problems/subsets-ii/
# https://leetcode.com/problems/subsets/
from typing import List

# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
#         res=[]
#         subset=[]
        
#         def dfs(i):
            
#             if i==len(nums):
#                 res.append(sorted(subset.copy()))
#                 return
#             #decision to include nums[i]
#             subset.append(nums[i])
#             dfs(i+1)
#             #decision NOT to include nums[i]
#             subset.pop()
#             dfs(i+1)
            
#         dfs(0)
#         res=set(map(tuple, res))
#         # res=list(map(list, res))
#         return res
    
# sol1 = Solution()
# output = sol1.subsetsWithDup([4,4,4,1,4])

# print (output)
class Solution:
 
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()
        subset=[]
        
        def dfs(i):
            
            if i==len(nums):
                res.append(subset.copy())
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            
            #decision NOT to include nums[i]
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i=i+1
            dfs(i+1)
            
        dfs(0)
    
        return res

    
sol1 = Solution()
output = sol1.subsetsWithDup([4,4,4,1,4])

print (output)

# def maximum_importance (S, M, N):

#     # Write your code here

#     s=[i for i in S]
#     s.sort()
#     print(s)

#     res =[]
#     def dfs(i,subset):

#         if i==N:
#             res.append(subset.copy())
#             return
        
#         subset.append(s[i])
#         dfs(i+1,subset)

#         subset.pop()
#         while i+1<N and s[i]==s[i+1]:
#             i=i+1
#         dfs(i+1,subset)

#     dfs(0,[])
    
#     # print(res)
#     data1=[]
#     data2=[]
#     for i in res:
#         if len(i)==M :
#             data1.append(i)
#         if len(i)==(N-M):
#             data2.append(i)
#     # print(data1)
#     # print(data2)
    
    
#     for i in data1:
#        temp=s.copy()
#        for j in range(len(i)):
#            temp.remove(i[j])
#        temp.sort()
#        print(temp)
    

# out_ = maximum_importance('allen', 2, 5)
# print (out_)