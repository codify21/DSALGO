#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:53:57 2021

@author: macbookpro
"""

from  collections import deque
import numpy as np
class Solution:
    def orangesRotting(self, grid):
        fresh, rotten = set(), deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        result = 0
        # pairs = [(1, 0), (-1, 0),(0, 1),  (0, -1)]
        while fresh and rotten:
            print(fresh,rotten)
            for i in range(len(rotten)):
                i,j = rotten.popleft()
                
                for index in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if index in fresh:
                        fresh.remove(index)
                        rotten.append(index)
                        
                        
            result += 1
                        
        # print(fresh)
        return -1 if fresh else result
        
     
        
sol1 = Solution()
image = [[2,1,1],[1,1,0],[0,1,1]]
# image = [[2,1,1],[0,1,1],[1,0,1]]
# image=[[0,2]]
# image=[[2,0,1,1,1,1,1,1,1,1],[1,0,1,0,0,0,0,0,0,1],[1,0,1,0,1,1,1,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,0,0,1,0,1],[1,0,1,0,1,1,0,1,0,1],[1,0,1,0,0,0,0,1,0,1],[1,0,1,1,1,1,1,1,0,1],[1,0,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
print(np.array(image))
output = sol1.orangesRotting(image)
print (output)


