#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 00:14:58 2021

@author: macbookpro
"""

class Node():
    
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild =  None
        self.rightChild = None

class AVL:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        self.root = self.insertNode(data,self.root)
        
    def insertNode(self,data,node):
        
        if not node:
            return Node(data)
        
        if data<node.data:
            node.leftChild = self.insertNode(data,node.leftChild)
        else:
            node.rightChild = self.insertNode(data,node.rightChild)
            
        node.height =  max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild))+1
        
        return self.settleViolation(data,node)
    
    def settleViolation(self,data,node):
        
        balance = self.calcBalance(node)
        
        #Case 1 : Left left heavy situation
        if balance >1 and data<node.leftChild.data:
            print('Left Left Heavy Situation')
            return self.rotateRight(node)
        if balance<-1 and data>node.rightChild.data:
            print('Right Right Heavy Situation')
            return self.rotateLeft(node)
        if balance>1 and data >node.leftChild.data:
            node.leftChild = self.rotateLeft(node.leftChild)
            print(' LEFT Heavy Situation')
            return self.rotateRight(node)
        if balance<-1 and data<node.rightChild.data:
            print('RIGHT Heavy Situation')
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node
        
    def calcHeight(self,node):
        if not node:
            return -1
        # print(node.height)
        return node.height
    
    def calcBalance(self,node):
        if not node:
            return 0
    
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)
    
    def outHeight(self,data):
        # print(self.root.data)
        self.root=self.outputHeight(data,self.root)
    
    def outputHeight(self,data,node):
        if not node:
            return -1
        
        if data == node.data:
            node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild))+1
            print(node.height)
            # return node.height
                
        if data<node.data:
            node.leftChild = self.outputHeight(data,node.leftChild)
            
        if data>node.data:
            node.rightChild = self.outputHeight(data,node.rightChild)
        
        
        
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
                           
    
    #if it returns value>1 it means it is a heavy left tree --> right rotation
    #if it ....         <1                  .... right tree --> left rotation
   
    
    def rotateRight(self , node):
        print('rotating to the right on node',node.data)
        
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        
        tempLeftChild.rightChild = node
        node.leftChild = t
        
        # node = tempLeftChild
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild))+1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild))+1
        
        return tempLeftChild
    
    def rotateLeft(self , node):
        print('rotating to the Left on node',node.data)
        
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild
        
        tempRightChild.leftChild = node
        node.rightChild = t
        
        # node = tempLeftChild
        
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild))+1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild))+1
        
        return tempRightChild
    
    def traverse(self):
        if self.root:           
            return self.traverseInorder(self.root)
    
    def traverseInorder(self,node):
        if node.leftChild:
            return self.traverseInorder(node.leftChild)
        print(node)
        if node.rightChild:
            return self.traverseInorder(node.rightChild)
        
        
    
tree = AVL()
# tree.insert(24)
# tree.insert(30)
# tree.insert(28)
# tree.insert(27)
# tree.insert(10)
# tree.insert(55)
# tree.insert(1)
# tree.insert(16)
# tree.insert(19)

# tree.outHeight(28)
tree.insert(10)
tree.insert(1)
tree.insert(19)
tree.insert(23)
tree.insert(16)
tree.insert(12)
