# # # import numpy as np
# # # arr = np.array([1, 3, 2, 4, 5])
# # # print(arr.argsort()[3:][::-1])
# #
# #
# #
# #
# #
# # l=[2,3,55,66,77,45]
# #
# #
# # for i in range(1,len(l)):
# #     j = i
# #     while j>0 and (l[j-1]>l[j]):
# #         temp = l[j]
# #         l[j] = l[j-1]
# #         l[j-1]= temp
# #
# #         j = j-1
# #
# # # print(l[-2])
# #
# #
# # nums=[2,3,55,66,77,45]
# #
# #
# # def mergesort(nums):
# #
# #     if len(nums)==1:
# #         return nums
# #
# #     mid = len(nums)//2
# #
# #     left_half = nums[0:mid]
# #     right_half = nums[mid:]
# #
# #     mergesort(left_half)
# #     mergesort(right_half)
# #
# #     i,j,k=0,0,0
# #
# #     while i<len(left_half) and j <len(right_half):
# #         if left_half[i]<=right_half[j]:
# #             nums[k]=left_half[i]
# #             i=i+1
# #         else:
# #             nums[k]=right_half[j]
# #             j=j+1
# #         k=k+1
# #
# #     while i<len(left_half):
# #         nums[k]=left_half[i]
# #         i=i+1
# #         k=k+1
# #
# #     while j<len(right_half):
# #         nums[k]=right_half[j]
# #         k=k+1
# #         j=j+1
# #
# #     return nums
# #
# #
# #
# # print(mergesort(nums))
# #
# #
# #
# #
#
#
# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b = b
#
#
#     def sum_no(self):
#         ans = self.a+self.b
#         return ans
#
#
# class B (A):
#
#     def __init__(self,a,b):
#         self.a = a
#         self.b=b
#     def sum_no(self):
#         ans = self.a-self.b
#         return ans
#
#
# # a = A(5,7)
# # print(a.sum_no())
# b=B(5,7)
# print(b.sum_no())
#
#
#
#
# create table contact (id autoincrement, userid varchar(100), mob_1 varchar(10) ,mob_2 varchar(10) ,pager varchar(20)
# primary_key (id) foreignkey(id ) references user(id)  ) ;
#
# create table user (id autoincrement , name varchar(30) , address  varchar(100) primary key (id))
#
#
#
#
#
#
#
# select count(user_id) from contact where ((mob1 is not null & mob2is not null) or
#
#                                    (mob2 is not null & pager is not null) or
#
#                                    (mob21 is not null & pager is not null))








#



# def sum1(a,b):
#     add = a+b
#     return add
#
#
#
# print(sum1(5,6))
#
#
# def sum1(a,b):
#     add = a*b
#     return add
#
#
#
# print(sum1(5,6))



Input = [10,1,2,7,6,1,5]
target = 8

def getting_sum(arr,target):
    res = []


    for i in range(len(arr)):
        check = target-arr[i]
        out = [arr[i]]
        if check in arr:
            out.append(check)
        if len(out)!=1:
            res.append(out)

    return res


    # for i in range(len(arr)):
    #     add_flag = arr[i]
    #     if arr[i]>target:
    #         continue
    #     out = [arr[i]]
    #     for j in range(i+1,len(arr)):
    #
    #         add_flag = arr[i]+arr[j]
    #         if add_flag<target:
    #             out.append(arr[j])
    #
    #     if add_flag ==target:
    #         res.append(out)
    #
    # return res


print(getting_sum(Input,target))









































