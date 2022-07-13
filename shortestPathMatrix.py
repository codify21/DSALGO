#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 00:15:56 2021

@author: macbookpro
"""
# https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/
# https://www.youtube.com/watch?v=vn-Jol8SNsM
from typing import List
from collections import Counter,deque


class Solution:
     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:        
        m,n=len(grid),len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        q=deque()
        visited=set()
        
        if grid[0][0]==0:
            q.append((1,(0,0)))
            # visited.add(0,0)
            grid[0][0]=1
        
        while q:
            steps,tmp=q.popleft()
            row,col = tmp[0],tmp[1]
            
            if (row,col)==(m-1,n-1):
                return steps
            for i,j in dirs:
                new_row = row+i
                new_col = col+j
                
                if (0<=new_row<m and 0<=new_col<n and grid[new_row][new_col]==0 
                    and (new_row,new_col) not in visited):
                    q.append((steps+1,(new_row,new_col)))
                    #visited.add(new_row,new_col)
                    grid[new_row][new_col]=1
                    
        return -1                    

sol1 = Solution()
output = sol1.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])

print (output)