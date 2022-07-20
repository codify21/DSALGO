#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 00:46:24 2022

@author: macbookpro
"""

# https://www.youtube.com/watch?v=o811TZLAWOo

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        
        dummy = ListNode(0,head)
        prev=dummy
        # curr=head
        
        while head and head.next:
            #save pointers befor splitting
            nxtPair = head.next.next
            second = head.next
            
            #reverse the pairs
            second.next=head
            head.next=nxtPair
            prev.next = second
            
            #update pointers after splitting
            prev=head
            head=nxtPair
            
        return dummy.next
          