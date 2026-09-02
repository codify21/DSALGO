#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:07:27 2021

@author: macbookpro
"""
import time

start = time.time()

class Solution:  
    def climbStairs(self, n: int) -> int:   # Dynamic Programming
    
        dp =[]
        
        dp.append(1)
        dp.append(2)
        
        for i in range(2,n):
            dp.append(dp[i-1]+dp[i-2])
        
        
        return dp[n-1]
    
       # def climbStairs(self, n: int) -> int:
       #    if n==1:
       #        return 1
       #    elif n==2:
       #        return 2
        
       #    first ,second=1,2
        
       #    for i in range(3,n+1):
       #        sum = first+second
       #        first ,second = second ,sum,
        
       #    return sum
        
        # def climbStairs(self, n: int) -> int:  # Fibonaccii way(stacks) : very slow
        #        if n==1:
        #           return 1
        #        elif n==2:
        #           return 2  
             
        #        else:            
        #           return (self.climbStairs(n-2)+self.climbStairs(n-1))
    
    
    
    

s = Solution()
fibonacci = s.climbStairs(40)
print(fibonacci)
end = time.time()
print(end - start)
