#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:13:27 2022

@author: macbookpro
"""

from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hashmap={}
        for edge in tickets:#creating a hashmap
            a,b=edge
            if a not in hashmap:
                hashmap[a]=[]
      
            hashmap[a].append(b)        
        # print(hashmap)       
        #sorting the hashmap values for lexical ordering
        for key,values in hashmap.items():           
                values.sort()
                hashmap[key]=values
        print(hashmap)
       
        res=['JFK']
                        
        def dfs(src):
            if len(res)==len(tickets)+1:
                return True
            if src not in hashmap:
                return False
        
            temp = hashmap[src]
        
            for i ,v in enumerate(temp):
                hashmap[src].pop(i)
                res.append(v)
            
                if dfs(v):return True
            
                hashmap[src].insert(i,v)
                res.pop()
            return False
        
        dfs('JFK')
        return res

    
sol1 = Solution()
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
output = sol1.findItinerary(tickets)
# output = sol1.findJudge(4,[[1,3],[1,4],[2,3]])
print(output)