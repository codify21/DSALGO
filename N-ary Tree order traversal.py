#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 03:43:48 2022

@author: macbookpro
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
from collections import deque,defaultdict
class Solution:
    def levelOrder(self, root):
#         level = defaultdict(list)     
#         queue = deque([root])
#         res=[]
     
#         def bfs(node,height):
#             if not node :
#                 return
#             level[height].append(node.val)
#             for child in node.children:
#                 queue.append(child)
#                 bfs(queue.popleft(),height+1)
        
#         bfs(queue.popleft(),0)
#         # print(level)      
#         for i in level:
#             res.append(level[i])
#         return(res)
        
        level=defaultdict(list)
        res=[]
        def dfs(node,height):
            if not node: return
            level[height].append(node.val)
            for child in node.children:
                dfs(child,height+1)
        dfs(root,0)
        for i in level:
            res.append(level[i])
        return(res)
    

            