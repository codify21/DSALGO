#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:24:59 2021

@author: macbookpro
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
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
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
                
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data)
        
    def traverse(self):
        if self.root:
            return self.traversePreOrder(self.root)
        
       
    def traversePreOrder(self,node):
         print(node.data)
         if node.leftChild:
             self.traversePreOrder(node.leftChild)
         if node.rightChild:
             self.traversePreOrder(node.rightChild)
             
    def twosum(self,k):
        return self.findTarget(self.root,k)
             
    def findTarget(self, node ,k):
        if not node.leftChild and not node.rightChild:
            return False
        
        output = self.dfs(node,k,node)
        if output:
            print("We have a combo")
        else:
            print("No Combo")
  
    def isNumberPresent(self,node,value,root):
        if root == None:
            return False
        print(root.data)
         # To not consider same node again! => node != root
        if node == root:
                return False
        if value<root.data:
            return self.isNumberPresent(node,value,root.leftChild)
        elif value>root.data:
            return self.isNumberPresent(node,value,root.rightChild)
        else:
            return True
       
    def dfs(self,node,k,root):
        
        if node == None:
            return None
        first = node.data
        value =  k-first
        # out = self.isNumberPresent(value,node)
        # print(out)

        if self.isNumberPresent(node,value,root):
            return ( True)
        
        
        return(self.dfs(node.leftChild,k,root) or self.dfs(node.rightChild,k,root) )
        
       
            
tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(6)
tree.insert(2)
tree.insert(4)
tree.insert(12)
# tree.traverse()
output = tree.twosum(6)


#DFS approach for creating list

class Solution:
    def findTarget(self, root, k):
        lst=[]
        def makelist(root,lst):
            if root:
                lst.append(root.val)
                if root.left:
                    makelist(root.left,lst)
                if root.right:
                    makelist(root.right,lst)
                    
        
        makelist(root,lst)
        print(lst)
        for i in range (0,len(lst)):
            if (k-lst[i]) in lst and lst.index((k-lst[i]))!=i:
                return True
        return False 

#3rd Way - Creating list using inorder traversal

class Solution:
    def findTarget(self, root ,k) :
        inList = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inList.append(node.val)
            inorder(node.right)
            
        inorder(root)
        l, r = 0, len(inList)-1
        
        while l < r:
            total = inList[l] + inList[r]
            if total == k:
                return True
            elif total < k:
                l += 1
            else:
                r -= 1
        return False

