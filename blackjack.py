# -*- coding: utf-8 -*-

# getting blackjacjk count 
Dict = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
        'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':11}
keys_list = list(Dict)
print(keys_list)

jack= ["four","ace","ten"]
sum=0
max=0
flag=0
card=''


for i in jack:
    sum= sum+Dict[i]
    if max<= Dict[i]: # getting the card with max value
        max=Dict[i]
        card=i
    if sum>21 and 'ace' in jack:
       sum=sum-11+1    
       flag=1
   
if flag==1: # getting the bigger value if ace is found in list and sum>21
    for i in range(11,1,-1):   
        if keys_list[i] in jack :
            card = keys_list[i]
            break
 
            
print (sum,card)

if sum==21:
    print ('blackjack',card)
elif sum>21:
    print('above',card)
else:
    print('below',card)

