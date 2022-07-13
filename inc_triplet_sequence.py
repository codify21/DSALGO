#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:15:06 2022

@author: macbookpro
"""
# https://www.youtube.com/watch?v=xZ5FBqk-cFw&t=148s
# https://leetcode.com/problems/increasing-triplet-subsequence/
from typing import List
from itertools import permutations

from collections import Counter,deque
import math

import copy
class Solution:  
     def increasingTriplet(self, nums: List[int]) -> bool:
         first = second = float('inf') # Initialize two variables to infinite
         for n in nums: # Loop through all numbers
            if n <= first: # If it is less then infinite you know you got the first triplet
                first = n
            elif n <= second: # If it is less then infinite you know you got the second triplet
                second = n
            else: # If its not less then the first and second then you know its the last value your looking for.
                return True
        

                
sol1 = Solution()
b=[12,11,15,2,16,18]
output = sol1.increasingTriplet(  b)
print(output)
