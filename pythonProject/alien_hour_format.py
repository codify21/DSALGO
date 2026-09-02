#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 05:59:47 2022

@author: macbookpro
"""
# https://www.techgig.com/codegladiators/question/cklySmdtS0tVanJoWWVRSDJSQXpLZndyaG44eWRNZ1Q4WEh5UXBBRHpFeitWYmt4OWlCVUJLRTRSSEpCa0UvRw==/1?msg_type=1#

# World Army vs Aliens (100 Marks)

# The world is going to be attacked by the aliens. The space intelligence department has raised an alarm and the world armies are coming together to fight them. The planning and strategizing is being done to make the maximum impact on the alien ships. The deadly missiles are to be put into action. The missiles are targeted to destroy the alien ships in space and disable them to land on the Earth.

# The army is planning to launch the attack at A time (hh mm) to get an advantage. For each attack, they know the time the missile will require to hit the coming alien ship. They all are busy in preparation and want to know the time at which the blast will occur and the alien ship will be destroyed in pieces. Can you find the time of the blast ?

# Note: The World Army follows a 24-hour time format and you need to find the time of blast accordingly. The time will be in the hh mm format.

# Input Format
# The first line of input consists of the launch time in hh mm format separated by space.
# The second line of input consists of the travel time for the missile in hh mm format separated by space.


# Constraints
# 00<= hh <=23
# 00<= mm <=59


# Output Format
# Print the time at which the blast will occur and the spaceship will be destroyed.


class calculate_time:

    def blast():
        first_input=input()
        second_input = input()

        a,b= first_input.split()
        a,b= int(a),int(b)
        c,d= second_input.split()
        c,d= int(c),int(d)
        
        # print(a,b,c,d)

        hour=[i for i in range(24)]
        print(hour)
        minute = [i for i in range(60)]
        print(minute)
       
        flag=0
        minute_sum = b+d
        actual_minute = minute_sum
        if minute_sum>=60:
            actual_minute = int(minute_sum%60)
            flag=1
        if actual_minute in hour[0:11] :
            actual_minute='0'+str(actual_minute)
        print(minute_sum,'minute_sum')
        print(actual_minute,'actual minute')
            
        hour_sum = a+c+flag
        print(hour_sum,'hou_sum')
        if hour_sum>=24:
            hour_sum = int(hour_sum%24)
            
        actual_hour = hour[hour_sum]
        if actual_hour in hour[0:11] :
            actual_hour='0'+str(actual_hour)

        return (actual_hour,actual_minute)

if __name__ == "__main__":
    hh,mm = calculate_time.blast()
    hh=str(hh)
    mm=str(mm)
    print(hh,mm)