#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 11:19:02 2022

@author: macbookpro
"""
# https://leetcode.com/problems/word-pattern/submissions/
from typing import List

class Solution:  
    def wordPattern(self, pattern: str, s: str) -> bool:
        res= {}
        s=s.split(' ')
        # res[s[0]]=pattern[0]
        # print(res)
        if len(s)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in res.keys() :
                if res[pattern[i]]==s[i]:
                    continue
                else:
                    return False
            else:
                if s[i] in res.values():
                    return False
                else:
                    res[pattern[i]]=s[i]
                print(res)
        return True
       
sol1 = Solution()
output = sol1.wordPattern("abbc","dog cat cat dog")
print(output)