#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:21:15 2021

@author: macbookpro
"""
# https://leetcode.com/problems/min-stack/submissions/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.size = 0
        

    def push(self, val: int) -> None:
        if self.size==0:
            self.min.append(val)
        else:
            if val<=self.min[-1]:
                self.min.append(val)
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        tmp = self.stack.pop()
        self.size -= 1
        if tmp == self.min[-1]:
            self.min.pop(-1)
        
        
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

