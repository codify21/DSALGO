#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 03:12:37 2021

@author: macbookpro
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            raise ValueError("Queue is empty!")
  
        if len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop(0))
        
        return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            raise ValueError("Queue is empty!")
            
        return self.stack1[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (len(self.stack1) + len(self.stack2) == 0)
        
    def traverse(self):
   
        print('Available Queue',self.stack1)
        print('Available Queue',self.stack2)

obj = MyQueue()
obj.push(10)
obj.push(20)
obj.traverse()
print('Object popped',obj.pop())
obj.push(30)
obj.traverse()
print('Object peeked',obj.peek())
obj.push(40)
obj.traverse()
print('Object popped',obj.pop())
obj.traverse()
print('Queue Empty:',obj.empty())