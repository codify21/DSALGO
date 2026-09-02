#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 20:21:38 2022

@author: macbookpro
"""


# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import copy
from itertools import permutations
from typing import List

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        l3 = ListNode()
        temp=l3
        carry = 0
        
        while l1 or l2 or carry:
            
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1+v2+carry #calcuating sum 
            carry = val//10
            val = val%10
            l3.next = ListNode(val)
            
            l3= l3.next #setting linked list pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return temp.next
    
#      def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         data1,data2='',''
#         while(l1) is not None:
#             # print(l1.data)
#             data1=data1+str(l1.val)
#             l1 = l1.next
#         while(l2) is not None:
#             # print(l2.data)
#             data2=data2+str(l2.val)
#             l2 = l2.next
#         data1=int(data1[::-1])
#         data2=int(data2[::-1])
         
#         res =str(data1+data2)  
#         res=(res[::-1])
#         # print(res)
#         l3=ListNode(int(res[0]))
#         temp=l3
#         for i in range(1,len(res)):
#             l3.next=ListNode(int(res[i]))
#             l3=l3.next
#             # print(l3.data,l3.next) 
#         return temp
            
                
                