#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 09:42:17 2022

# @author: macbookpro
# """

# https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/1473226/Python-DFS-and-UnionFind-and-BFS-with-explanation -  All 3 solutions
# https://leetcode.com/problems/find-if-path-exists-in-graph/discuss/1511658/Simple-Solution-DFS

from typing import List
import copy
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashmap={}
        for edge in edges:
            a,b=edge
            if a not in hashmap:
                hashmap[a]=[]
            if b not in hashmap:
                hashmap[b]=[]
            hashmap[a].append(b)
            hashmap[b].append(a)
        print(hashmap)
        
        visited = set()
        
        def hasPath(hashmap,src,dst,visited):
            if src==dst:
                return True
            if src in visited:
                return False
            visited.add(src)
            
            for neighbor in hashmap[src]:
                if hasPath(hashmap,neighbor,dst,visited)== True:
                    return True
            return False
        
        return hasPath(hashmap,source,destination,visited)
    
    
sol1 = Solution()
output = sol1.validPath(3,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,1]],  0,  3)
print(output)
output = sol1.validPath(3,[[0,1],[0,2],[3,5],[5,4],[4,3]],  0,  3)
print(output)


#To print all the paths b/w two nodes
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashmap={}
        for edge in edges:
            a,b=edge
            if a not in hashmap:
                hashmap[a]=[]
            if b not in hashmap:
                hashmap[b]=[]
            hashmap[a].append(b)
            hashmap[b].append(a)
        # print(hashmap)
        # hashmap=[[1,2],[3],[3],[]]- Another question
# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/
        # print(hashmap)
        # visited = set()
        res=[]
        def hasPath(hashmap,src,dst,visited):
            if src==dst:
                visited.append(src)
                res.append(visited.copy())
                visited.remove(src)
                return True
            if src in visited:
                return False
            
            visited.append(src)
            
            for neighbor in hashmap[src]:
                # print(neighbor)
                hasPath(hashmap,neighbor,dst,visited)
                # print(data)
            visited.remove(src)
        
        
        hasPath(hashmap,source,destination,[])
        return(res) 
        
sol1 = Solution()
output = sol1.validPath(3,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,1]],  0,  3)
print(output)
output = sol1.validPath(3,[[0,1],[1,2],[2,0]],  0,  2)
print(output)




