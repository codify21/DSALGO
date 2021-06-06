#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 10:47:42 2021

@author: macbookpro
"""
# https://leetcode.com/problems/longest-palindromic-substring/submissions/
from typing import List
import time
start = time.time()


class Solution:
    # def longestPalindrome(self, s: str) -> str: # Brute Force My Method
    #       # s=list(s)
    #       palindrome=[]
    #       flag=0
    #       for i in range(len(s)-1):
    #         for index in range(i+1,len(s)):
    #             try:
    #                 if s[i]==s[index]:
    #                 # index = s.index(s[i],i+1)
    #                 # print(index)
    #                 # print(s[i+1:index])
    #                 # print(s[index-1:i:-1])
    #                   orignal = s[i+1:index]
    #                   revers = s[index-1:i:-1]
    #                   if orignal==revers:
    #                       flag=1
    #                       palindrome.append(s[i:index+1])
    #             except:
    #                 continue
    #       palindrome.sort(key=len,reverse=True)
    #       print(palindrome)
    #       if flag==1:
    #         return palindrome[0]
    #       else:
    #             return s[0]
            
    def longestPalindrome(self, s: str) -> str:#expand fom middle
        if s=='' or len(s)<1:
            return ''
        start , end = 0,0
        for i in range(len(s)):
            len1 = self.expandfFromMiddle(s,i,i)
            len2 = self.expandfFromMiddle(s,i,i+1)
            print('len',len1,len2)
            length = max(len1,len2)
            if(length>end-start):
                start = i - int((length-1)/2)
                end = i+int(length/2)
            print('start',start,end)
        return s[start:end+1]
       
        
       
    def expandfFromMiddle(self,s,left,right):
       
        if (s=='' or left>right):
            return False
        while(left>=0 and right<len(s) and s[left]==s[right]):
            left=left-1
            right = right+1
        print('l/r',left,right)
        return right-left-1
         
             
         
            
        # xdxtfdaarvvznrptwicdldmrmwbdrmyppvamdvofujthfcmkcugvodmlvubgvodectwzparprifwgwfvddlrfdnrpspirtyvxqvbqiglugbmzoyzcfkvbjdrdqqxxzutebgoacczuhopvzjfrnfsylgfgkbmbjqqyggtdjcvjbvpspkjcezanajjzabfidndfdpkuamwvxrbpxzoivlnkwdxedtfnmvicmzebwktpktokibeycbpqzejddwnvimmbzupyxwmrgdbmcujadfexcchdkfvkxsdwkuwuxzhpnjgmqbmidcwywjgcsbydixyxcclcbrzjvrmlrzgmbviifllouykovscaufvxovwmmgubshtoizbwtcpqzwchtkmkjfneuybfglywfrorhmfdgvjdsmegtoytsivnuaceszpfsxgddbweckgziahkslykgdkztmpapnoyawqtyrdcuzaxcohohapektyfbfhrsdnjbgjvwvqpcikdnlkdogsinkfpymkkdburnbksnqfjgjlacqpfqlhsjhhoccdkrjipqwzsxmpjughaqchzlrqkogkryqkuuxhzchovebzgeekuflcgvxugnxcvugqlstmnljlvxonkybmzjmnsvvwfztcplgikptnppbzeygbmdsyimsntveojwsejmastiovbctdkdlfvpyzihhxishtveflnmamlnzqroxknrrkkfpveyzvvasdznykygrpbfkbinrrvheekeumlvlgalqelspvpiydqkwduckimyhpzsxlcpkbvgwmwnasdxuupdhcmxjoushcvcnjyrmuemuydyywpvzhkxsqszaqhnbhjwsokkpployomoawtr
        
s = Solution()
longestPalindrome = s.longestPalindrome("abaaba")
print(longestPalindrome)
end = time.time()
print(end - start)
