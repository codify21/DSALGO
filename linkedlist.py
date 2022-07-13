#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 01:21:28 2021

@author: macbookpro
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head= None
        self.size =0
        
    def insertStart(self,data):
        node = Node(data)
        self.size+=1
        
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        # print(self.head.data)
        
    def insertEnd(self,data):
        temp = self.head
        node = Node(data)
        # print(temp.data)
        # print(temp.next)
        while temp.next is not None:
            temp = temp.next
        temp.next = node
    
    def display(self): 
        temp = self.head
        # print(temp.data)
        while temp is not None:
            print(temp.data)
            temp = temp.next
            # print(temp.next)
        self.middleNode(self.head)
        
        
        
    def middleNode(self, head):
        l = []  #MORE Practical APPROACH
        while head:
            l.append(head)
            head = head.next
        # print(l)
        index = len(l) // 2
        print ("Middle Node is",l[index].data)

ll = LinkedList()
# ll.insertStart(4)
# ll.insertEnd(5)
ll.insertStart(3)
ll.insertEnd(6)
ll.insertEnd(7)
ll.insertEnd(8)
ll.insertEnd(9)
ll.display()
# ll.middleNode(Node(3))
# mid = middleNode(ll.head)


# https://leetcode.com/problems/design-linked-list/
#try to correct linkedlist deletion part
# class Node:
#     def __init__(self,val,next=None):
#         self.val=val
#         self.next= next

# class MyLinkedList:

#     def __init__(self):
#         self.head = None
#         self.size = 0
        

#     def get(self, index: int) -> int:
#         if index<0 or index>=self.size:
#             return -1
#         prev=None
#         count=0
#         temp=self.head
#         while count<=index:
#             prev=temp
#             temp=temp.next
#             count+=1
#         return prev.val
        
#     def addAtHead(self, val: int) -> None:
#         if self.head is None:
#             self.head = Node(val)
            
#         else:
#             node = Node(val)
#             node.next = self.head
#             self.head= node
#         self.size+=1
        

#     def addAtTail(self, val: int) -> None:
        
#         if self.head is None:
#             self.head = Node(val)
            
#         node=Node(val)
#         temp=self.head
#         while(temp.next):
#             temp= temp.next
#         temp.next=node
#         self.size+=1
        

#     def addAtIndex(self, index: int, val: int) -> None:
#         if index>self.size:
#             return
#         elif index<=0:
#             self.addAtHead(val)
#         elif index == self.size:
#             self.addAtTail(val)
#         else:    
#             node = Node(val)
#             temp =self.head
#             prev = Node(0,temp)
#             count=0

#             while count<index:
#                 prev=prev.next
#                 temp=temp.next
#                 count+=1
#             node.next = temp
#             prev.next = node          
#             self.size+=1


#     def deleteAtIndex(self, index: int) -> None:
#         if index<0 or index>=self.size:
#             return
#         if self.size==1:
#             self.head = None
#             return
#         prev = None
#         temp=self.head
#         count=0
#         if index==1:#for head position
#             self.head=self.head.next
            
#         if index<self.size:#if index in middle
#             while count<index:
#                 prev=temp
#                 temp=temp.next
#                 count=count+1
#             prev.next = temp.next
            
#         if index>=self.size:#if index at last
#             while count<index:
#                 prev=temp
#                 temp=temp.next
#                 count=count+1
#             prev.next = None
#         self.size-=1
        
#     def display(self): 
#         temp = self.head
#         # print(temp.data)
#         while temp is not None:
#             print('data',temp.val)
#             temp = temp.next
#             # print(temp.next)
        
# l = MyLinkedList();
# l.addAtHead(1);
# l.deleteAtIndex(0);
# l.display()

# # l.addAtTail(3);
# # l.addAtIndex(1, 2);    #// linked list becomes 1->2->3

# # l.get(1);              #// return 2
# # l.deleteAtIndex(1);    #// now the linked list is 1->3
# # l.display()

# # l.get(1);              #// return 3