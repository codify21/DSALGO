#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 02:02:06 2022

@author: macbookpro
"""
from typing import List


from collections import Counter

import copy
#using hashmap and two pointers
class Solution:  
    def partitionLabels(self, s: str) -> List[int]:
    
        global res,hashmap,string
        string = s
        res=[]
        output = []
        hashmap = Counter(s)
         
        forward = 0
        backward= self.backward_func(s[forward])
        # print(backward)
         
        while(forward<len(s)):
            backward = self.helper(forward,backward)
            forward = backward+1
            if forward>=len(s):
                break
            backward= self.backward_func(s[forward])
        
        #after running above loop we have partitioned the string and appended the strings in res list
        print(res)
        for i in res:
            output.append(len(i))
        return(output)

    def helper(self,forward,backward):
        flag=0
        sub_string = string[forward:backward+1]
        temp = Counter(sub_string)
        # print(temp)
         
        for data,value in temp.items():
            # print(data,value)
            if hashmap[data]==value:
                continue
            else:
                flag=1
                break
        if flag==1:#used to increase the size of window until we have a substring whose size satisfy our condition of each letter appears in atmost one part.
            backward = backward+1
            backward= self.helper(forward,backward)
            return backward
        else:
            res.append(sub_string)
            return backward   
         
    def backward_func(self,forward):
        words=copy.copy(string)
         # reversing the list
        words= words[::-1]
        
        # finding the index of element
        index = words.index(forward)
        
        # printing the final index
        return(len(words) - index - 1)
    
class Solution:  
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex={}
        
        for i,c in enumerate(s):
            lastIndex[c]=i
        # print(lastIndex)
        res = []
        size,end=0,0
        
        for i,c in enumerate(s):
            size+=1
            end=max(end,lastIndex[c])
            
            if i ==end:
                res.append(size)
                size=0
        return res
    
sol1 = Solution()
output = sol1.partitionLabels("ababcbacadefegdehijhklij")
# ababcbacadefegdehijhklij
print (output)