#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:04:46 2021

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
                
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data,self.root)
            # print('Root',self.root.data)

    
    def removeNode(self,data,node):
        
        if not node:
            return None
        
        if data<node.data:
            node.leftChild = self.removeNode(data,node.leftChild)# to update the refrences
        elif data>node.data:
            node.rightChild = self.removeNode(data,node.rightChild)
        else:
            
            if not node.leftChild and not node.rightChild:
                print('Removing a leaf node ....')
                del node
                return None
            
            if not node.leftChild:
                print('Removing a node with single right child')
                tempNode = node.rightChild
                del node
                return tempNode
            elif not node.rightChild:
                print('Removing a node with single left child')
                tempNode = node.leftChild
                del node
                return tempNode                 
            
            print('Removing node with 2 children')
            # tempNode = self.getPredecessor(node.leftChild)
            # node.data= tempNode.data
            # node.leftChild = self.removeNode(tempNode.data,node.leftChild)
            
            tempNode = self.getSuccessor(node.rightChild)
            node.data= tempNode.data
            node.rightChild = self.removeNode(tempNode.data,node.rightChild)
            # print('actual',node.rightChild.data) 
        return node
            
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)        
        return node
    
    def getSuccessor(self,node):
        if node.leftChild:
            return self.getSuccessor(node.leftChild)        
        return node
                           
    def getMinValue(self):
        if self.root:
            return self.get_min(self.root)
            
    def get_min(self,node):
        
        if node.leftChild:
            return self.get_min(node.leftChild)
        
        return node.data
       
    def getMaxValue(self):
        if self.root:
            return self.get_max(self.root)
            
    def get_max(self,node):
        
        if node.rightChild:
            return self.get_min(node.rightChild)
        
        return node.data
       
    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)
        
    def traverseInOrder(self,node):  # O(n) --  Time complexity
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)
            
    def traversePreOrder(self,node):
        print(node.data)
        if node.leftChild:
            self.traversePreOrder(node.leftChild)
        if node.rightChild:
            self.traversePreOrder(node.rightChild)
    def traversePostOrder(self,node):
        
        if node.leftChild:
            self.traversePostOrder(node.leftChild)
        if node.rightChild:
            self.traversePostOrder(node.rightChild)
        print(node.data)


tree = BST()
tree.insert(32)
tree.insert(10)
tree.insert(55)
tree.insert(1)
tree.insert(16)
tree.insert(19)
tree.insert(17)
tree.insert(79)
tree.insert(18)
tree.insert(14)


print('Max',tree.getMaxValue())
print('Min',tree.getMinValue())  
tree.traverse()
a=tree.remove(16)
# print('hello',a.data)
tree.traverse()
