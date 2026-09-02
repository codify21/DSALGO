#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 02:42:36 2022

@author: macbookpro
"""

# https://www.youtube.com/watch?v=82A7Je0dHFA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        dummy= slow=ListNode(0,head) # 0(1) Space complexity
        # slow= dummy
        while head:
            if head.next and head.val==head.next.val:
                while head.next and head.val==head.next.val:
                    head=head.next
                slow.next=head.next
            else:
                slow =slow.next
            head=head.next
        
        return dummy.next
                
        
#         temp=[] #basic Approach using more space
#         curr=head
        
#         while curr:
#             temp.append(curr.val)
#             curr=curr.next
        
#         c = Counter(temp)
#         temp=[data for data,value in c.items() if value==1 ]
        
#         dummy =curr= ListNode()
        
#         for i in temp:
#             curr.next = ListNode(i)
#             curr=curr.next
        
#         return dummy.next

        
        
        
        