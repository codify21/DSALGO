#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:50:17 2021

@author: macbookpro
"""
# https://leetcode.com/problems/flood-fill/
class Solution:

    def floodFill(self, image, sr, sc, newColor):
       
        
        color = image[sr][sc]
 
        def fill(i,j):
            if i <0 or j<0 or i>= len(image) or j>=len(image[0]):
                return 
            elif image[i][j] != color or image[i][j] == newColor:
                return 
            image[i][j] = newColor
            
            fill(i, j+1)
            fill(i, j-1)
            fill(i+1, j)
            fill(i-1, j)
        fill(sr,sc)
        return image
    
    
    # ## 2nd Approach
    #     color=image[sr][sc]
    #     row ,col = len(image),len(image[0])
    #     # print(row,col,color)
 
    #     def dfs(r,c):
    #         print(r,c)
    #         if (image[r][c]==color):
    #             image[r][c]=newColor
    #             if r>=1 : dfs(r-1,c)
    #             if r+1<row :dfs(r+1,c)
    #             if c>=1 : dfs(r,c-1)
    #             if c+1<col: dfs(r,c+1)
                
    #     dfs(sr,sc)
    #     print( image )
                
       
    
sol1 = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
output = sol1.floodFill(image,sr,sc,newColor)
print( output )