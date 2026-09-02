#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 20:59:28 2022

@author: macbookpro
"""

from typing import List

def find_boundary(arr: List[bool]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    
    left =0
    right = len(arr)-1
    boundary_index=-1
    
    
    while left<=right:
        
        mid = (left+right)//2
        
        if arr[mid]==False:
            left=mid+1
        
        else:
#             else arr[mid]==True:
            right = mid-1
            boundary_index=mid
            
    return boundary_index
        
                

if __name__ == '__main__':
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)

