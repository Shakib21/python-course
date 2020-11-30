#!/usr/bin/env python
# coding: utf-8

def bubbleSort(mylist): 
    n = len(mylist) 
  
    
    for i in range(n): 
  
         
        for j in range(0, n-i-1): 

            if mylist[j] > mylist[j+1] : 
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j] 
    return mylist


mylist = [34,346,123,6,42,123,56,23,4]


bubbleSort(mylist) 


mylist




