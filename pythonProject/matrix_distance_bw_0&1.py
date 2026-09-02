#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 01:55:31 2021

@author: macbookpro
"""
# https://leetcode.com/problems/01-matrix/

import collections

class Solution:
    def updateMatrix(self, mat):
        row = len(mat)
        col = len(mat[0])
        queue = []  # queue = collections.deque()

        pairs = [(1, 0), (-1, 0),(0, 1),  (0, -1)]

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    # adding only the indexes and not values{0}
                    queue.append((i, j))#two brackets coz deque.append() takes exactly one argument 
                else:
                    mat[i][j] = -1
        print(queue)
        while queue:
            rem = queue.pop(0)#rem = queue.popleft()
            row = rem[0]
            col = rem[1]
            print(row, col)
            for index in pairs:
                rowdash = row+index[0]
                coldash = col+index[1]

                if rowdash >= 0 and coldash >= 0 and rowdash < len(mat) and coldash < len(mat[0]) and mat[rowdash][coldash] < 0:
                    queue.append((rowdash, coldash))
                    mat[rowdash][coldash] = mat[row][col]+1
                    
        return mat


sol1 = Solution()
image = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]

output = sol1.updateMatrix(image)
print (output)
