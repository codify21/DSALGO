#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:15:38 2022

@author: macbookpro
"""
# https://leetcode.com/problems/repeated-dna-sequences/
# Same type question- https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result={}
        output=[]
        for i in range(0,len(s)-10+1):
            sub_string = s[i:i+10]
            
            if sub_string in result:
                result[sub_string]+=1                
            else:
                result[sub_string]=1
                
        for key,value in result.items():
            if value>1:
                output.append(key)
        
        return output

#     def findRepeatedDnaSequences(self, s: str) -> List[str]:
#         length = 10
#         seen = set()
#         ans = set()
#         for i in range(len(s)-length+1):
#             seq = s[i:i+length]
#             if seq in seen:
#                 ans.add(seq)
#             else:
#                 seen.add(seq)
#         return list(ans)
            
sol1 = Solution()
output = sol1.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print (output)