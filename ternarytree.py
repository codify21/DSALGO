#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 04:28:59 2021

@author: macbookpro
"""

class Node:
    def __init__(self,character):
        self.character = character
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None
        self.value = 0
        
class TST:
    def __init__(self):
        self.rootNode = None
    
    def put(self,key,value):
        self.rootNode  = self.putItem(self.rootNode,key,value,0)
        
    def putItem(self,node,key,value,index):
        
        temp = key[index]
        
        if node == None:
            node = Node(temp)
            
        if temp < node.character:
            node.leftNode = self.putItem(node.leftNode,key,value,index)
        elif temp > node.character:
            node.rightNode = self.putItem(node.rightNode,key,value,index)
        elif index < len(key)-1:
            node.middleNode = self.putItem(node.middleNode,key,value,index+1)
        else:
            node.value = value
        return node
    
    
    def get(self,key):
        
        node = self.getItem(self.rootNode,key,0)
        
        if node==None:
            return -1
        
        return node.value
    
    def getItem(self,node ,key,index):
        
        if node == None:
            return None
        
        temp = key[index]
        # print (node.character)
        
        if temp <node.character:
            return self.getItem(node.leftNode,key,index)
        elif  temp>node.character:
            return self.getItem(node.rightNode,key,index)
        elif index < len(key)-1:
            return self.getItem(node.middleNode,key,index+1)
        else :
            return node
        
        
        
if __name__ == "__main__":
    table = TST()
    table.put('cat',10)
    table.put('car',15)
    table.put('orange',20)
    table.put('apple',30)
    table.put('cow',40)
    
    print(table.get('cata'))
    
        
        
        
        
        
        
        
    
      