#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:31:27 2021

@author: macbookpro
"""

# https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    
    # def longestCommonPrefix(self, strs: List[str]) -> str:
        ###return os.path.commonprefix(strs)## shortest way to get common prefix
      
    #     min_length = min(strs,key=len)# min([len(i) for i in strs])
    #     min_length = len(min_length)
        
    #     first = strs[0]
    #     pre=''
        
    #     for i in range(1,len(strs)):
    #         for j in range(min_length):
            
    #             if (first[j]   == strs[i][j]):
    #                 pre = pre+strs[i][j]
    #             else:
                    
    #                 break          
    #         first = pre
    #         pre=''
    #     return first
    
      def longestCommonPrefix(self, strs: List[str]) -> str:
         if len(strs) == 0:
             return ""
         if len(strs) == 1:
             return strs[0]
        
         prefix = strs[0]
         prefix_len = len(prefix)
        
         for s in strs[1:]:
             while prefix != s[0:prefix_len]:
                 prefix = prefix[0:prefix_len-1]
                 prefix_len -= 1
                
                 if prefix_len == 0:
                     return ""
         return prefix
    
    
s = Solution()
prefix = s.longestCommonPrefix(["doggo",'doremi','disaster',"dog"])
print(prefix)
                    
                    