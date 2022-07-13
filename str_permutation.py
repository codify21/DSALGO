#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 02:16:51 2021

@author: macbookpro
"""

# 567. Permutation in String 
# https://leetcode.com/problems/permutation-in-string/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/ - Find all anagrams

from collections import Counter
class Solution:
    def checkInclusion(self, s1,s2):
        ls1 = len(s1)
        # hash1 = dict((i,1) for i in s1 )
        # print(hash1)
        s1_counter = Counter(s1)
        # print(s1_counter)
        window_counter = Counter()
        
        for i,c in enumerate(s2):
            # print(c)
            window_counter[c]+=1
            # print(window_counter)
            # print(i,ls1)
            if i>=ls1 :
                element_from_left = s2[i-ls1]
                
                if window_counter[element_from_left]==1:
                    del window_counter[element_from_left]
                else:
                    window_counter[element_from_left]-=1
            
            if window_counter == s1_counter:
                print( True)
            
        return False
    
sol1 = Solution()
s1 = "aba"
s2 = "eidbaaoo"
output = sol1.checkInclusion(s1,s2)
