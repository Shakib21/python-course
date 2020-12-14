#!/usr/bin/env python
# coding: utf-8
def checkprime(n):
    for i in range(2,round(n/2)):
        if n%i == 0:
            return False
    return True

def primenumbers(n):
    
    series = []
    i=2
    j=0
    while j<n:
        if(checkprime(i)):
            series.append(i)
            j+=1
        i+=1
            
    print(series)primenumbers(5)