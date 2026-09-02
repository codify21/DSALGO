#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 01:01:00 2021

@author: macbookpro
"""

class Node:
    def __init__(self,name):
        self.name= name
        self.adjacency_list=[]
        self.visited = False
        self.predecessor = None
        
class BreadthFirstSearch:
    
    def bfs(self,startNode):
        
        queue=[]
        queue.append(startNode)
        startNode.visited = True
    
        #BFS ->queue        DFS --> stack BUT usually we implement with recursion
        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)
            
            for n in actualNode.adjacency_list:
                if not n.visited:#n.visited is False
                    n.visited = True
                    queue.append(n)
                    
node1= Node('A')
node2= Node('B')
node3= Node('C')
node4= Node('D')
node5= Node('E')

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node3)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)
