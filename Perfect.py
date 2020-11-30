#!/usr/bin/env python
# coding: utf-8
def perfect(n):
    
    series = []
    num = 0
    
    for i in range(1,n):
        
        if n%i==0:
            num+=i
    
    if num == n:
        return True
    else:
        return False
            
    print(series)perfect(6)