

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






# data=[-5, -23, 5, 0, 23, -6, 23, 67]

# def swap(data,i,j):
#     temp = data[i]
#     data[i]=data[j]
#     data[j]=temp
    


# def sorting(nums):
    
    
#     for i in range(len(nums)):
        
#         j=i
        
#         while j>0 and nums[j-1]>nums[j]:
#             swap(nums,j,j-1)
#             j=j-1

#     return nums    


# second=sorting(data)
# print("Sorted list is ",second)



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




# def solution(root, l, c):     #  l -> level number  and  c -> column number
#             if root is None:
#                 return
#             mapp[(c,l)].append(root.val)
#             solution(root.left, l + 1, c - 1)
#             solution(root.right, l + 1, c + 1)
            
#         mapp = defaultdict(list)
#         solution(root, 0, 0)
#         res = []
#         old = float("-inf")
        
#         for k, v in sorted(mapp.items()):
            
#             if k[0] != old:   # to check whenever a new index/vertical column starts
#                 res.append([])
                
#             res[-1].extend(sorted(v))
#             old = k[0]
#         return res





# arr = [5,2,3,5,4,3]
# # [5,2,3][2,3,4,5],[5,4,3],[4,3][3]


# res=[]
# res1=[]

# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[j] not in res:
#             res.append(arr[j])
#         else:
#             break
#     res1.append(res)
#     res=[]
   
# print(res1)
# length=0
# flag=0
# for i in res1:
#     temp=len(i)
#     if temp>length:
#         length=temp
#         flag=i
        
# print(flag)










# def check_divide(func):
#     def inner(a,b):
#         if b==0:
#             print ("Division is not possible")
#         return func
        
        
#     inner()
    

# @check_divide
# def divide(a,b):
#     print('After division',(a/b))
    
    

# divide(5,7)






# comp = [i for i in range(1,10)]

# print(comp)




# class A:
    
#     def sum(self,a,b):
#          print(a+b)
         
# class B(A):
    
#     def sum(self,a,b):
#         return(a+b+10)
        
# test = B()
# print(test.sum(5,7))    





# select  A.id ,A.value ,B.value from  A, B  right join on A.id = B.id 



# class Publisher(models.Model):
    
#     name = models.TextAreaField()
#     security_no. = models.IntegerFied()
#     book = models.CharField()
#     Best_seller =models.BooleanField()
#     price=models.DoubleField()
    
    
    







class A:
    
    def summ(a,b):
        
        
        return a+b
    
class B(A):
    
    def summ(a,b):
        
        return a+b+10




lis= [3,4,3,4,5,1,5,2,3]


out = lis.sort()

item=out[-1]
flag=0
for i in range(len(lis)-1,-1,-1):
    if out[i]==item:
        flag+=1
        continue
    else:
        break
    
print("Occurence",flag)




















