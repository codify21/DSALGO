#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:12:02 2021

@author: macbookpro
"""
# https://leetcode.com/problems/build-an-array-with-stack-operations/

from typing import List
import time

start = time.time()

class Solution:
    # def buildArray(self, target: List[int], n: int) -> List[str]:
    #     stack =[]
    #     x=0
    #     list1 = [i for i in range(1,n+1)]
    #     print(list1)
    #     for i in range(len(target)):
    #         for j in range(x,len(list1)):
    #             if target[i] == list1[j]:
    #                 stack.append('push')
    #                 x= j+1
    #                 break
    #             else:
    #                 stack.append('push')
    #                 stack.append('pop')
    #     return stack
    
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res=[]
        t=1
        i=0
        while i<len(target):
            #print(target[i])
            #print("i val is " + str(i))
            if target[i]==t:
                res.append("Push")
                t=t+1
                i=i+1
            else:
                res.append("Push")
                res.append("Pop")
                t=t+1
        return res
    
    # def buildArray(self, target: List[int], n: int) -> List[str]:
    #     ops = []
    #     nt = []
    #     for i in range(1, n+1):
    #         if i in target:
    #             ops.append("Push")
    #             nt.append(i)
    #         else:
    #             ops += ["Push", "Pop"]
    #         if target == nt:
    #             return ops
                
    
        

s = Solution()
Array = s.buildArray(target = [1,7],n = 7)
print(Array)
end = time.time()
print(end - start)

    
        