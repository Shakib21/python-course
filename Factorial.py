#!/usr/bin/env python
# coding: utf-8
def factorial(n):
    
    f = 1
    for i in range (1,n+1):
        f*=i
    
    return f
factorial(7)