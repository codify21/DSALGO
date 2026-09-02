#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 02:02:12 2022

@author: macbookpro
"""

# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://www.youtube.com/watch?v=MVxvNunB0d4

from collections import defaultdict
class Solution:
    def averageOfLevels(self, root):
        Sum = defaultdict(float)
        Total_nodes = defaultdict(int)
        def dfs(node,h):
            
            if not node:
                return
            dfs(node.left,h+1)
            dfs(node.right,h+1)
            
            Sum[h]+= node.val
            Total_nodes[h]+= 1
        dfs(root,0)
        print(Sum)   
        res=[]
        for i in range(len(Sum)):
            res.append(Sum[i]/Total_nodes[i])
            
        return res
            
s = Solution()
reverse = s.averageOfLevels([3,9,20,15,7])
print(reverse)