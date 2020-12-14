#!/usr/bin/env python
# coding: utf-8

mylist = [6,1,3,7,4,2,5,9,8]



def sort(mylist):
    
    s = len(mylist)
    
    temp = 0
    
    for i in range(0,s):
        
        for j in range(i,s):
            
            if mylist[j] < mylist[i]:
                
                temp = mylist[j]
                mylist[j] = mylist[i]
                mylist[i] = temp
                
    return mylist


sort(mylist)



