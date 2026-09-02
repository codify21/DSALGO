#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 06:54:36 2021

@author: macbookpro
"""
# https://leetcode.com/problems/binary-tree-tilt/

from  collections import deque
import numpy as np

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.tilt = 0
        
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root == None:  # if not self.root
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)
    #O(logn) if the tree is balanced!!!! --> it can be reduced to O(n) --> AVL & RBT are needed
    def insertNode(self,data,node):
        
        if data<node.data:
            if node.left:
                self.insertNode(data,node.left)
            else:
                node.left = Node(data)
                
        else:
            if node.right:
                self.insertNode(data,node.right)
            else:
                node.right = Node(data)
                
    def traverse(self):
        if self.root:
            return self.traversePreOrder(self.root)
        
    def traversePreOrder(self,node):
        print(node.data)
        # print(node.tilt)
        if node.left:
            self.traversePreOrder(node.left)
        if node.right:
            self.traversePreOrder(node.right)
            
    def traverseTiltAnswer(self,node):
        # print(node.data)
        return(node.tilt)

        
# class Solution:
#     def findTilt(self, root):
        
#         if root.left:
#             # print(root.data)
#             self.findTilt(root.left)
        
            
#         if root.right:
#             # print(root.data)
#             self.findTilt(root.right)
            
#         if (not root.left) and (not root.right):
#             # print(root.data)
#             root.tilt=0
#             return 
      
#         if not root.left and root.right:
#             # print(root.data)
#             root.tilt = self.traversePreOrder(root.right,0)
#             return
        
#         if not root.right and root.left:
#             # print(root.data)
#             root.tilt = self.traversePreOrder(root.left,0)
#             return
          
#         if  root.right and root.left:  
#             # print(root.data,'replay')
#             # print(root.data)
#             data1=self.traversePreOrder(root.left, 0)
#             data2=self.traversePreOrder(root.right, 0)
#             # print(data1,data2,"dejaVu")
#             root.tilt = abs( data1-data2 )
#             return 
        
      
        
#     def traversePreOrder(self,node,data):
#         data = data+node.data
#         if node.left:
#              data = self.traversePreOrder(node.left,data)
         
#         if node.right:
#              data= self.traversePreOrder(node.right,data)
#         return data

class Solution:
    def findTilt(self, root):
        self.res = 0#global tilt sum
        
        def dfs(node):
            global result
            if not node: return 0  # if node is null return 0
			# traverse depth wise till we reach the leaf nodes
            
            leftSum = dfs(node.left)
            rightSum = dfs(node.right)
            result = abs(leftSum - rightSum)
            self.res =   self.res +result
            print(node.data,self.res,result)
            return node.data + leftSum + rightSum # return sum of left and right subtrees
            
        dfs(root)
        return result    

    
tree = BST()
tree.insert(21)
tree.insert(15)
tree.insert(10)
tree.insert(18)
tree.insert(35)
tree.insert(38)
tree.insert(36)
tree.insert(42)
# tree.insert(2)
# tree.insert(1)
# tree.insert(3)
tree.traverse()



print("*******")
# print(tree.root.data)
sol1 = Solution()
tilt = sol1.findTilt(tree.root)
# output = tree.traverseTiltAnswer(tree.root)
print (tilt)
