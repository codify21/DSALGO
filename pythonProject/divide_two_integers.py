#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 01:05:51 2021

@author: macbookpro
"""

from typing import List
import time
start = time.time()


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
   
        # while(dividend-divisor>=0):# general idea
        #     divide = divide+1
        #     dividend = dividend - divisor
        
        div=abs(dividend)
        diviso=abs(divisor)
        output=0
        while(div-diviso>=0):
            tmp = diviso
            count=1
            while(div-tmp>=0):
                div = div-tmp
                
                output=output+count
                count=count+count
                tmp=tmp<<1
                print('dividend',div,'output',output,'count',count,'tmp',tmp)
            
        if(dividend<0 and divisor>0)or (dividend>0 and divisor<0):
            output=-output
            
        return min((1<<31)-1,max((-1<<31),output))
    
s= Solution()
divide = s.divide(629,30)
print(divide)
end = time.time()
print(end - start)