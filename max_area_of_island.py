#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 04:08:29 2021

@author: macbookpro
"""
# https://leetcode.com/problems/max-area-of-island/

import numpy as np
class Solution:
    def maxAreaOfIsland(self, grid):
        num_rows, num_cols = len(grid), len(grid[0])
        area = 0
        
        def traverse_through_island(row, col):
            left, right, top, bottom = 0, 0, 0, 0
            print(row,col)
            if grid[row][col] == 1:
                grid[row][col] = -1 # negative 1 means we already visited this cell
                
                if row > 0: 
                    top = traverse_through_island(row-1, col) # for top neighbor
                if row < num_rows-1: 
                    bottom = traverse_through_island(row+1, col) # for bottom neighbor
                if col > 0: 
                    left = traverse_through_island(row, col-1) # for left neighbor
                if col < num_cols-1: 
                    right = traverse_through_island(row, col+1) # for right neighbor
                print(left, right, top, bottom)

                return left + right + top + bottom + 1
            
            return left + right + top + bottom # for all cells  with the value 0            
        
        # call the method traverse_through_island()
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    area = max(area, traverse_through_island(row, col))        
        print( "Max Area is ",area)

sol1 = Solution()
grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

image = [[1,0,0],[1,1,1],[0,0,0]]
print(np.array(image))
output = sol1.maxAreaOfIsland(image)