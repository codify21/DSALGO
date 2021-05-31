#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:58:51 2021

@author: macbookpro
"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.enq=[]
        self.deq=[]
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.enq.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if len(self.enq)>0:
            while (self.enq):
                self.deq.append(self.enq.pop())
        data=self.deq.pop(0)
        while len(self.deq)>0:
            self.enq.append(self.deq.pop())
        return data
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if len(self.enq)>0:
            while (self.enq):
                self.deq.append(self.enq.pop())
        data=self.deq[0]
        while len(self.deq)>0:
            self.enq.append(self.deq.pop())
        return data
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.deq)+len(self.enq)==0:
            return True
        return False
    
    def traverse(self):
   
        print('Available Queue',self.enq)
        print('Available Queue',self.deq)
         
        

obj = MyStack()
obj.push(10)
obj.push(20)
obj.traverse()
print('Object popped',obj.pop())
obj.push(30)
obj.traverse()
print('Object peeked',obj.top())
obj.push(40)
obj.traverse()
print('Object popped',obj.pop())
obj.traverse()
print('Queue Empty:',obj.empty())