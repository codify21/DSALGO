#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 03:36:28 2021

@author: macbookpro
"""

class Node:
    def __init__(self,name):
        self.name= name
        self.adjacency_list=[]
        self.visited = False
        self.predecessor = None
        
class DepthFirstSearch:
    
    def dfs(self,Node):
        
        Node.visited =True
        print(Node.name)
        
        for i in Node.adjacency_list:
            if not i.visited:
                self.dfs(i)
        
        
                    
node1= Node('A')
node2= Node('B')
node3= Node('C')
node4= Node('D')
node5= Node('E')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

dfs = DepthFirstSearch()
dfs.dfs(node1)
