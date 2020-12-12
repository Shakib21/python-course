#!/usr/bin/env python
# coding: utf-8

def checkprime(n):
    for i in range(2,round(n/2)):
        if n%i == 0:
            return 0
    return 1

def Prime(n):
    series = []
    for i in range(2,n-1):
        
        if n%i==0:
            if(checkprime(i)) and i!=4:
                series.append(i)
    print(series)

Prime(1935423)