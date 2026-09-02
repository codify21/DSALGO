#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 02:44:35 2022

@author: macbookpro
"""

class Solution:
    def numsSameConsecDiff(self, n, k) :
        
        res = set(i for i in range(1, 10))
        res1 = set()

        for _ in range(n -1):
            print(_)
            for x in res:
                print(res)
                if x % 10 + k < 10:
                    res1.add(x * 10 + x % 10 + k)
                if x % 10 - k >= 0:
                    res1.add(x * 10 + x % 10 - k)
            print('res1',res1)
            res = res1
            res1 = set()
        return list(res)
    



    # def numsSameConsecDiff(self, n, k):
    #         res = set()
    #         def dfs(curr, digit, step):
    #             nonlocal res
    #             if step == n:
    #                 res.add(curr)
    #                 return 
                    
    #             if digit - k >= 0:
    #                 dfs(curr * 10 + digit - k, digit - k, step + 1)
                    
    #             if digit + k <= 9:
    #                 dfs(curr * 10 + digit + k, digit + k, step + 1)
            
    #         for i in range(1, 10):
    #             dfs(i, i, 1)
    #         return list(res)
                
s = Solution()
reverse = s.numsSameConsecDiff(3,7)
print(reverse)