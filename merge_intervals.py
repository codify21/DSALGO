#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:45:53 2022

@author: macbookpro
"""
# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:  
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda intervals: intervals[0])
        print(intervals)
        output=[intervals[0]]
        for i in intervals[1:]:
            
            if i[0]<= output[-1][1]:
                output[-1][1]=max(i[1], output[-1][1])
            else:
                output.append(i)
        return output
              
sol1 = Solution()

output = sol1.merge( [[1,3],[2,6],[3,7],[8,10],[15,18]])
# output = sol1.merge([[1,4],[5,6]])
print(output)

# https://leetcode.com/problems/non-overlapping-intervals/submissions/
# https://www.youtube.com/watch?v=nONCGxWoUfM
class Solution:  
     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
            intervals.sort(key = lambda intervals: intervals[0])
            print(intervals)
            output=[intervals[0]]
            flag=0
            for i in intervals[1:]:
        #wil keep one which ends first as it minimises chance of overlapping
                if i[0]<output[-1][1]:
                    if i[1]<output[-1][1]:
                        output[-1]=i
                        
                    # else:
                    #     del i
                else:
                    output.append(i)
                print(output)
            print(output)
            
            intervals.sort()
            res =0 
            prevEnd = intervals[0][1]
            for start,end in intervals[1:]:
            
                if start>=prevEnd:#not overlapping 
                    prevEnd = end#therefore update the prevEnd value
                else: #if overlapping , remove one intervals
                    res+=1#upadte prevEnd and remove
                    prevEnd = min(end,prevEnd)
                
            return res
          
sol1 = Solution()
output = sol1.eraseOverlapIntervals(   [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]] )

# output = sol1.eraseOverlapIntervals(   [[1,100],[11,22],[1,11],[2,12]] )
# output = sol1.merge([[1,4],[5,6]])
print(output)