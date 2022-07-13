# # -*- coding: utf-8 -*-

# class c(object):

#     a=42
#     def __init__(self,a=6,b=7):
#         self.a =a
#         self.b =b
#     def do_print(self):
#         print('{}{}'.format(self.a,self.b))

# x=c(15)
# # x.do_print()
# import re
# txt = '11 degrees celcius is 51.8 degrees fahrenheit'

# # d= [s for s in txt.split() if s.isdigit()]
# # print (d)
# x = re.findall('[0-9]+', txt)
# print(x)

# for s, r in txt:
#     rr = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)
#     if rr == r:
#         print('GOOD')
#     else:
#         print('WRONG', rr, 'should be', r)


# def secondlast(s):
#     data = s.split(',')
#     print (data[-2])
# s= secondlast('Sales,Nashik,6 Feb 2020,233')


# def process_list(mylist):
#     return (sum([x for x in mylist if isinstance(x, int) if int(x%2)!=0]))

# def process_list(mylist):
#     return [x for x in mylist if isinstance(x, int)][-1:-5:-1]

# d = process_list([1, 3, 5, 15, 22, 'b'])
# print(d)
# print(d[-1:-5:-1])

# d=24
# print(type(d))
# if d is type(int):
# #     print('yes')
# add=0
# with open('input.txt') as fp:

#     for i in range (7):
#         line = fp.readline()
#         try:
#             line=int(line)
#         except :
#             add='Error'
#             break

#         if isinstance(line,int):
#             add=add+line
# print(add)

# def date1():
#     try:
#         date = input('enter the date in dd/mm/yyyy format')
#         # date = '05/02/2021'
#         data = date.split('/')
#         data[0] = '01'
#         output = '/'.join(data)
#         print(output)


#     except :

#         print('Enter the Correct date')
#         date1()

# correct_date = date1()


# import json,sys,socket,time
# f =open('config.json')

# data =json.load(f)

# LOG_FILENAME = "logfile.log"
# import requests
# import logging
# LOG_FILENAME = "logfile.log"

# def url_ok(url):
#     r = requests.get(url,timeout=2)
#     return r.status_code == 200

# def readingUrl():

#         for url in data['urls']:
#             # print (url)
#             response = url_ok(url)
#             print(response)
#             try:
#                 if response == False:
#                     logging.basicConfig(filename="logfile.log",
#                                  format='%(asctime)s %(message)s')
#                     logging.warning('Site is down {}'.format(url))
#             except requests.exceptions.ConnectTimeout as e :
#                 # print ("Timeout occurred")

#                 logging.warning('Site is not accessible {}'.format(url))
#                 pass
#             except Exception as e:

#                 logging.warning('Site is not accessible {}'.format(url))
#                 print(e)
#                 pass
#         time.sleep(data['interdata'])


# while True:
#     readingUrl()


# import json,sys,socket,time
# import requests
# import logging
# import traceback
# from urllib3.exceptions import NewConnectionError as new
# s=socket.socket()

# f =open('config.json')
# data =json.load(f)
# LOG_FILENAME = "logs.log"

# def url_ok(url):
#     r = requests.get(url)
#     return r.status_code == 200

# def readingUrl():
#         logging.basicConfig(filename=LOG_FILENAME,format='%(asctime)s %(message)s')
#         logger=logging.getLogger()
#         logger.setLevel(logging.WARNING)

#         for url in data['urls']:
#             # print (url)
#             try:
#                 response = url_ok(url)
#                 print(response)

#                 if response == False:
#                     logger.error('Site is down ',url)
#                     pass

#             except requests.exceptions.ConnectionError as e :
#                 print(1)
#                 print ("Timeout occurred")
#                 logger.warning('Site is not accessible {}'.format(url))
#                 pass
#             except requests.exceptions.Timeout as e:
#                 print(2)
#                 logger.warning('Site is not accessible {}'.format(url))
#                 # print (e)
#                 pass
#             except requests.exceptions.RequestException as error:
#                 print(2.5)
#                 logger.warning('Site is not accessible {}'.format(url))
#                 pass
#             except requests.exceptions.ConnectTimeout as e:
#                 print(3)
#                 print ("Timeout occurred")
#                 pass
#             except Exception as e:
#                 print(4)
#                 logger.warning('Site is not accessible {}'.format(url))
#                 print(e)
#                 pass
#         time.sleep(data['interdata'])

# while True:
#     readingUrl()


# def barterMarket(comicBooks, coins, coinsNeeded, coinsOffered):
#     print(comicBooks, coins, coinsNeeded, coinsOffered)
#     fiction = 0
#     while((coins-coinsNeeded)>=0 and comicBooks>0):
#         coins = coins-coinsNeeded
#         fiction = fiction+1
#         comicBooks = comicBooks-1
#     # print(fiction,comicBooks)
#     # if (comicBooks>1 and coins<coinsNeeded):
#     #     coins = coins+coinsOffered
#     #     comicBooks = comicBooks-1
#     #     return barterMarket(comicBooks, coins, coinsNeeded, coinsOffered)
#     return(fiction)


# z= barterMarket(4,8,4,3)

# # z= barterMarket(3,6,4,5)
# # z= barterMarket(393,896,787,920)
# print(z)


# a=[1,2,3,4,2,3] -- 2
# b=[1,2,3,4,3,2] -- 3
# c=[1,2,3,4]  --  -1

# def duplicate(a):

#     d={}
#     c=0

#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]==a[j]:

#                 d[a[i]]=(j-i)
#                 c=c+1
#                 break

#     print(d)

#     if(c==0):
#         print(-1)
#     else:

#         out = sorted(d.items(), key=lambda x: x[1])
#         print(out[0][0])


# dup = duplicate([1,2,3,4,2,3])


# def getMaxToys(N, P, y ,x, toys):
#     start = P
#     x_lt = [i for i in x if i<start][-1]
#     x_gt = [i for i in x if i>start][0]
#     # print(x_lt,x_gt)


# # out_ = getMaxToys(4, 0, 4, [-5,-1,2,5], [10,2,3,4])#out =5
# out_ = getMaxToys(10, 9, 15, [-18,-6,-1,1,7,11,12,16,17,20], \
#                   [77,50,73,86,57,50,6,37,91,76])#out = 307

# 443
# T = int(input())
# for _ in range(T):
#     N ,P, k = map(int, input().split())
#     x = list(map(int, input().split()))
#     toys = list(map(int, input().split()))

#     out_ = getMaxToys(N, P, k, x, toys)
#     out_ = getMaxToys(4, 0, 4, [-5,-1,2,5], [10,2,3,4])


#     print (out_)

# class test:
#     def a(self):
#         print("class test")

# class test1:
#     def a(self):
#         print("class test1")

# class test2(test1,test):
#     def a(self):
#         super(test2,self).a()
    
# t2=test2()
# t2.a()
# test1().a()

# # def ask():
# #     flag=True
# #     while flag:
# #         try: 
        
# #             val = int(input('Enber the input'))
# #             print(type(val))
# #             if type(val) ==int:
# #                 flag=False
# #                 break
# #         except:
# #             print('wrong entry: Try again')
# #             ask()
# #     print('User correct')
# # ask()

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

# print(output)



# l = ['word1','word2','word3']

# # string ="random"
# rev=""

# for j in l:
#     rev=""
#     for i in range(len(j)-1,-1,-1):
#         rev =rev+j[i]
        
#     print(rev)
    
    
    
    
def binary_search(values,data):
    left=0
    right = len(values)
    
    
    while(left<right):
        
        mid=int((left+right)/2)
        # print(mid)
        
        if(data>values[mid]):
            left = mid+1
            
        elif(data<values[mid]):
            right = mid-1
            
        else:
            return mid
    
output = binary_search([1,2,3,4,5],4)
print(output)

   




























            
