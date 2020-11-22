#!/usr/bin/env python
# coding: utf-8

#example function

def add(a,b):
    print(a+b)
    add(1,2)
x=1
y='2'

#the try method
try:
    
    add(x,y)

except:
    print('Erroe :)')
else:
    print('Add went well')
    