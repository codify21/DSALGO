#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 02:21:56 2022

@author: macbookpro
"""

# https://www.youtube.com/watch?v=nPVEaB3AjUM

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # return [math.comb(rowIndex,i) for i in range(rowIndex+1)]
        
        res=[[1]]
        for i in range(rowIndex):
            temp = [0]+res[-1]+[0]
            row=[]
            for j in range(len(res[-1])+1):
                row.append(temp[j]+temp[j+1])
            res.append(row)

        return res
# T = [[1]*(i+1) for i in range(r+1)]

        
sol1 = Solution()
output = sol1.getRow(3)

print (output)