

# from typing import List
# from itertools import permutations

# from collections import Counter,deque
# import math
# import pprint
# import copy
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        

        
        

    
# sol1 = Solution()
# tickets = 
# output = sol1.findItinerary(tickets)

 











# select * from employees where salary =(
# select min(salary) from employees where salary in  
# (select distinct top 5 salary in employees order by desc))






# Reverse the sequence without changing the position of the 
# special characters sequence - `123$456&789^0&`
# Output: '098$765&432^1&'



# special =['$','&','^','`']
# data = "123$456&789^0&"

# def split(word):
#     return [char for char in word]
     
# # Driver code
# word = 'geeks'
# # print(split(word))
# data=(split(data))
# print(data)
# print(len(data))

# for i in range(len(data)):
#     for j in range(int(len(data)-1)/2,-1,-1):
#         print(data[j])
#         if data[i] in special:
#             break
#         if data[j] in special:
#             continue
#         if data[i] not in special and data[j] not in special:        
            
            
            
#             temp =data[i]
#             data[j] =temp
#             temp=data[i]
        
        
        
# print(data)







# https://www.youtube.com/watch?v=4xbWSRZHqac
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
        
# #         l,r = 0,len(nums)-1
# #         i=0
        
# #         def swap(i,j):
# #             temp=nums[i]
# #             nums[i]=nums[j]
# #             nums[j]=temp
            
# #         while i<=r:
# #             if nums[i]==0:
# #                 swap(l,i)
# #                 l+=1
# #             elif nums[i]==2:
# #                 swap(r,i)
# #                 r-=1
# #                 i-=1# to nullify a special case where 0 might come in b/w your array
# #             i+=1
        
#         counter= Counter(nums)
#         result = []
#         start = 0 
#         for i in range(3):
#             end = start+counter[i]
#             for j in range(start, end):
#                 nums[j] = i 
#             start = end
        
        






