

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






data=[-5, -23, 5, 0, 23, -6, 23, 67]

def swap(data,i,j):
    temp = data[i]
    data[i]=data[j]
    data[j]=temp
    


def sorting(nums):
    
    
    for i in range(len(nums)):
        
        j=i
        
        while j>0 and nums[j-1]>nums[j]:
            swap(nums,j,j-1)
            j=j-1

    return nums    


second=sorting(data)
print("Sorted list is ",second)



# names = Employee.objects.filter(Q(name__startswith="s")|Q(name__endswith='y'))


# Table1 =  Employee  ,  TABLE2 = Order

# select Employee.name , Order.value
# from Employee inner join Order on Employee.empcode = Order.empcode



# class Post:
#     posts=models.CharField()
    
# Class Users:
#     name = 
#     email = models
#     posts = models.ForeignKey(Post,null =True)
    
    

# posts = User.objects.filter(post)




        

