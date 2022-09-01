#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 16:35:07 2022

@author: macbookpro
"""
import numpy
class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        M,N=len(matrix),len(matrix[0])
        
        for i in range(M):   #Transposing matrix in-place
            for j in range(i+1,N):
                
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
              
        # print(matrix)   
        
        # for i in range(M):
        #     for j in range(N//2):
        #         temp=matrix[i][j]
        #         matrix[i][j]=matrix[i][N-1-j]
        #         matrix[i][N-1-j]=temp
        # print(matrix)   
        
        matrix[:] = [i[::-1] for i in matrix]
        print(matrix) 
                
sol1 = Solution()
nums= [1,2,3,4,5,6,7]
output = sol1.rotate([[1,2,3],[4,5,6],[7,8,9]])