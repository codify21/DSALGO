#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 01:27:24 2021

@author: macbookpro
"""

class Heap:
    heap_size=10
    
    
    def __init__(self):
        self.heap = [0]*10
        self.current_position = -1
        
    def insert(self,item):
        
        if self.isFull():
            print('Heap is Full..')
            return
        self.current_position = self.current_position+1
        self.heap[self.current_position] = item
        self.fixUp(self.current_position)
        
    def fixUp(self,index):
        parentIndex = int((index-1)/2)
        while parentIndex >=0 and self.heap[parentIndex]<self.heap[index]:
          
            temp = self.heap[parentIndex]
            self.heap[parentIndex] = self.heap[index]
            self.heap[index] = temp
            index = parentIndex
            parentIndex = int((index-1)/2)
            
    def heapSort(self):
        
        for i in range(0,self.current_position+1):
            temp = self.heap[0]
            print(temp)
            self.heap[0] = self.heap[self.current_position-i]
            self.heap[self.current_position-i] = temp
            self.fixDown(0,self.current_position-i-1)
            
    def fixDown(self,index,upto):
        while index<=upto:
            leftChild = 2*index+1
            rightChild  = 2*index+2
            
            if leftChild<=upto:  # or if rightChild<upto:  Both will work
                childToSwap = None
                
                if rightChild>upto: # this case comes handy when after 1st reconstruction 
                #there is still need for more reconstruction
                    childToSwap = leftChild
                else:
                    if self.heap[leftChild]>self.heap[rightChild]:
                        childToSwap=leftChild
                    else:
                        childToSwap = rightChild
                        
                if self.heap[index]<self.heap[childToSwap]:
                    temp = self.heap[index]
                    self.heap[index]= self.heap[childToSwap]
                    self.heap[childToSwap] = temp
                else:
                    break
                
                index = childToSwap
                
            else:
                break
        
            
            
    def isFull(self):
        if self.current_position == Heap.heap_size:
            return True
        else:
            return False
        
if __name__=="__main__":
    heap = Heap()
    heap.insert(100)
    heap.insert(23)
    heap.insert(210)
    
    heap.insert(90)
    heap.insert(5)
    
    heap.insert(300)
    heap.insert(325)

    
    heap.heapSort()
