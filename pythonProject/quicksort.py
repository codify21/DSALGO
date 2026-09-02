#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 02:41:21 2021

@author: macbookpro

QUICKSORT AND SELECTION SORT AND MERGE SORT
"""

# def quick_sort(nums,low,high):
    
#     if low>high:# Base Condition 
#         return
    
#     pivot = partition(nums,low,high)
#     quick_sort(nums,low,pivot-1)  #recursively calling for sorting left and right subarray
#     quick_sort(nums,pivot+1,high)
    
# def partition(nums,low,high):
#     pivot_index = (low+high)//2
#     swap(nums,pivot_index,high)
    
#     i = low
    
#     for j in range (low,high,1):
#         if nums[j]<=nums[high]: # use > for descending algo 
#             swap(nums,i,j)
#             i=i+1
    
#     swap(nums,i,high)
    
#     return i
    
# if __name__=="__main__":
#     nums=[-1,2,3,2,1,0,-2,4]
#     quick_sort(nums,0,len(nums)-1)
#     print(nums)
    
def swap(nums,i,j):
    temp=nums[i]
    nums[i]=nums[j]
    nums[j]=temp
    
#selection Sort

def select(nums):
    
    for i in range (0,len(nums)-1):      
        index = i# To find the index of smallest no. in 1 run
        for j in range(i+1,len(nums),1):
            
            if(nums[j]<nums[index]):
                # temp =nums[i]
                # nums[i]=nums[j]
                # nums[j]=temp
                index=j#shifting of index by 1 after 1 sort and so on
        if index!=i:
            swap(nums,index,i)
    return nums
    
if __name__=="__main__":
    num=[-1,2,3,2,1,-2,0,-2,4,-3]
    print(select(num))

#Insertion Sort

def insertion(nums):   
    
        for i in range(1,len(nums)):#insertion Sort
            j=i
            while j>0 and nums[j-1]>nums[j]:
            
                swap(nums,j,j-1)
                j=j-1
        return nums
                
    

# def mergesort(nums):
    
#     if len(nums)==1:
#         return
#     middle = len(nums)//2
    
#     left_half = nums[:middle]
#     right_half = nums[middle:]
    
#     mergesort(left_half)
#     mergesort(right_half)
    
#     i=0 # for left_half subarray
#     j=0 # for right_half subarray
#     k=0 # for result array 
    
#     while(i<len(left_half)) and (j<len(right_half)):
#         if left_half[i]<right_half[j]:
#             nums[k]=left_half[i]
#             i=i+1
#         else:
#             nums[k]=right_half[j]
#             j=j+1
#         k=k+1
        
#     while i<len(left_half):
#         nums[k]=left_half[i]
#         k=k+1
#         i=i+1
    
#     while j<len(right_half):
#         nums[k]=right_half[j]
#         k=k+1
#         j=j+1
        

# if __name__=="__main__":
#     nums=[-1,2,3,2,1,0,-2,4]
#     mergesort(nums)
#     print(nums)
    