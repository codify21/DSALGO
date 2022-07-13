#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 05:23:00 2022

@author: macbookpro
"""
# https://www.youtube.com/watch?v=BJnMZNwUk1M&t=32s

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left,right = 0,len(matrix[0])
        top,bottom = 0,len(matrix)
        
        while left<right and top<bottom:
            
            #get every i in top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            #get every i in right column
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            #to check boundaries
            if not(left<right and top< bottom):
                break
            #get every i in bottom row
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            #get every i in left column
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            
        return res

sol1 = Solution()
output = sol1.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print (output)

            
            
            
        