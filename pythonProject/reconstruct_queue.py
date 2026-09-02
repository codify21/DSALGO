#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 04:46:48 2021

@author: macbookpro
"""
# https://leetcode.com/problems/queue-reconstruction-by-height/
from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        # for i in range(len(people)):
        #     for j in range(len(people)):
                
        #         if people[i][0]>people[j][0]:
        #             temp= people[i]
        #             people[i]=people[j]
        #             people[j]=temp
        # return people
                    
                    
        
    
        
        people= sorted(people,key=lambda x:(-x[0],x[1]))
        #sorting the array w.rt. 1st elemnt in decreasing and 2nd element increasing respectivley
        res=[]
        for p in people:
            res.insert(p[1],p)
            #inserting element [i,j] from people to position j in res
        return res
        
        
s = Solution()
reconstruct= s.reconstructQueue([[7,0],[4,4],[7,1],[6,4],[5,0],[6,1],[5,2]])
print(reconstruct)    
        
