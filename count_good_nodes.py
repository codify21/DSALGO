#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:03:11 2022

@author: macbookpro
"""

# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class Solution:
    def goodNodes(self, root) :
        # if root.left is None and root.right is None:
        #     return 1
        
        def dfs(node,count,max_so_far):
            
            if node is None:
                return count
            
            if node.val>= max_so_far:
                max_so_far=node.val
                count = count+1
            
            count = dfs(node.left,count,max_so_far)
            count = dfs(node.right,count,max_so_far)
        
            return count
        
        return dfs(root,0,root.val)