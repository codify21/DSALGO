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
#             				 	format='%(asctime)s %(message)s')
#                     logging.warning('Site is down {}'.format(url))
#             except requests.exceptions.ConnectTimeout as e :
#                 # print ("Timeout occurred")
                
#                 logging.warning('Site is not accessible {}'.format(url))
#                 pass
#             except Exception as e:
                
#                 logging.warning('Site is not accessible {}'.format(url))
#                 print(e)
#                 pass
#         time.sleep(data['interval'])


# while True:
#     readingUrl()



import json,sys,socket,time
import requests
import logging
import traceback
from urllib3.exceptions import NewConnectionError as new
s=socket.socket()

f =open('config.json')
data =json.load(f)
LOG_FILENAME = "logs.log"

def url_ok(url):
    r = requests.get(url)
    return r.status_code == 200

def readingUrl():
        logging.basicConfig(filename=LOG_FILENAME,format='%(asctime)s %(message)s')
        logger=logging.getLogger()
        logger.setLevel(logging.WARNING)

        for url in data['urls']:
            # print (url)
            try:
                response = url_ok(url)
                print(response)
                           
                if response == False:
                    logger.error('Site is down ',url)
                    pass
                
            except requests.exceptions.ConnectionError as e :
                print(1)
                print ("Timeout occurred")                
                logger.warning('Site is not accessible {}'.format(url))                
                pass
            except requests.exceptions.Timeout as e: 
                print(2)
                logger.warning('Site is not accessible {}'.format(url))
                # print (e)
                pass
            except requests.exceptions.RequestException as error:
                print(2.5)
                logger.warning('Site is not accessible {}'.format(url))
                pass
            except requests.exceptions.ConnectTimeout as e:
                print(3)
                print ("Timeout occurred")
                pass
            except Exception as e:
                print(4)
                logger.warning('Site is not accessible {}'.format(url))
                print(e)
                pass
        time.sleep(data['interval'])

while True:
    readingUrl()












