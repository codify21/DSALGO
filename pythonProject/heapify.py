#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 02:41:47 2021

@author: macbookpro
"""
#with the help of heapify we are able to create array representation of a heap tree like structure
from heapq import heappop , heappush ,heapify

heap = []
nums =[12,3,-2,0,9,45,10,88,33]

heapify(nums) # No ordering Here
print(nums)



for num in nums:
    heappush(heap,num)

while heap:
    print(heappop(heap))
    
    # PYTHON BUILTS A MIN HEAP