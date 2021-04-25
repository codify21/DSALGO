#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 21:30:04 2021

@author: macbookpro
"""

class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     r,num,y=0,0,0
        
    #     y = x              
    #     while(x>0):
    #         r = x%10
    #         x =int(x/10)
    #         num = num*10 + r
        
    #     if num == y :
    #         return True
    #     else:
    #         return False 
        
    
        def isPalindrome(self, x: int) -> bool:
            y = str(x)          
            rev = y[::-1]
            
            if rev == y :
                return True
            else:
                return False 
                
            
            
     
    
        
s = Solution()
isPalindrome = s.isPalindrome(212)
print(isPalindrome)