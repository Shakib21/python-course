#!/usr/bin/env python
# coding: utf-8
def checkprime(n):
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True


def sieve(limit):
    
    mylist = []
    
    for i in range(0,limit+1):
        
        if(checkprime(i)):
            mylist.append(i)
    
    print(mylist)


sieve(1000)