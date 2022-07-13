#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 05:44:28 2021

@author: macbookpro
"""

#here we discuss about Linear Probing
class hashTable:
    def __init__(self):
        self.size=10
        self.keys= [None]*self.size
        self.values = [None]*self.size
    def hashfunction(self,key):#transforming keys(any object-string float custom object)
                               # to  array indices
        add=0
        for pos in range(len(key)):
            add =add +ord(key[pos])#returns the unicode code point for 1 character string : a->97 
        return add%self.size
    
    def put(self,key,data):# to insert values in array
        index = self.hashfunction(key)
        
        #not None : Its a collision
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = data #update
        
            #rehash: try to find another slot
            index = (index+1) #or (index+1)%self.size
        #insert    
        self.keys[index]=key
        self.values[index] = data
        
    def get(self,key):# to return values in array
        index = self.hashfunction(key)
 
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index] 
        
            #if there is a chance of collision thats why we update index by +1
            index = (index+1)%self.size
            
    def all(self):
        for i in self.values :
            print(i)
            
if __name__ == "__main__":
    table = hashTable()
    table.put('apple',10)
    table.put('apple',15)
    table.put('orange',20)
    table.put('peaches',30)
    table.put('kiwi',40)
    
    # print(table.get('apple'))
    table.all()