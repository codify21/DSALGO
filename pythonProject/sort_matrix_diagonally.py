#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 23:34:20 2022

@author: macbookpro
"""
# https://www.youtube.com/watch?v=gBMrhTptVG0

import heapq,heapify
from collections import defaultdict
class Solution:
    def diagonalSort(self, mat) :
        
        M,N = len(mat),len(mat[0])
        
        new_mat=[]
        #Creating new matrix to store all values of each diagonal from bottom-left           corner to right topmost corner
            
        #for this we need to use 2 loops 2 times first for lower half then upper half
        
        #lower half
        for i in range(M-1,0,-1):
            r,c=i,0
            tmp=[]
            while r<M and c<N:
                tmp.append(mat[r][c])
                r+=1
                c+=1
            new_mat.append(sorted(tmp))
        #upper half                  
        for j in range(N):
            r,c=0,j
            tmp=[]
            while r<M and c<N:
                tmp.append(mat[r][c])
                r+=1
                c+=1
            new_mat.append(sorted(tmp))
        
        print(new_mat)
        
        output=[]
        
        for row in range(M):
            i=0
            tmp=[]
            for k in range(len(new_mat)):
                if i>=N:break
                if new_mat[k]==[]:
                    continue
                cand = new_mat[k].pop()
                tmp.append(cand)
                i+=1
            print(tmp)
            output.append(tmp)
        print(output)
        #we are getting output in reversed form so reverse the output to 
        # match as per your requirement
        return((output[::-1]))
        
        
        # 2nd Way
        new_mat = defaultdict(list)
        
        for row in range(M):
            for col in range(N):
                heapq.heappush(new_mat[row-col],mat[row][col])
        
        print(new_mat)
        
        for row in range(M):
            for col in range(N):
                mat[row][col]=heapq.heappop(new_mat[row-col])
                
        return mat
                
        
        
sol1 = Solution()
output = sol1.diagonalSort( [[3,3,1,1],[2,2,1,2],[1,1,1,2]])
print(output)