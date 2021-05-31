# -*- coding: utf-8 -*-
# Have the function EvenPairs(str) take the str parameter being passed and determine if a pair 
# of adjacent even numbers exists anywhere in the string. If a pair exists, return the string 
# true, otherwise return false. For example: if str is "f178svg3k19k46" then 
# there are two even numbers at the end of the string, "46" so your program should return 
# the string true. Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so 
# your program should return the string true.


import re
even=[]

def EvenPairs(strParam):
   str_list = re.findall("\d*", strParam)#re.findall("[0-9]", strParam)
   str_list = list(filter(None, str_list))#removing null values from list
   str_list= length(str_list)#calling length function to get only no.s with length more than 2
   print(str_list)
   
   for i in range(len(str_list)):
       for j in range(len(str_list[i])-2):
          
           a=str_list[i][j]
           b=str_list[i][j+1]
           c=str_list[i][j+2]
           if int(a)%2==0 and int(b)%2==0:
               print(1)
               print (int(a),int(b))
               break
           if int(a)%2==0 and (int(b)*10+int(c))%2==0:
               print(2)
               print (int(a),int(b)*10+int(c))
               break
       
   

           
        
def length(strlist):
    for i in range(len(strlist)):
        if len(strlist[i])>1:
            even.append(strlist[i])
            
    return even
            
   


# keep this function call here 
print(EvenPairs("3gy41d216"))