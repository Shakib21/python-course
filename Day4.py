#!/usr/bin/env python
# coding: utf-8


square = lambda num: num**2

mynums = [9,9]

list(map(lambda num: num**2,mynums))

check_even = lambda num: num%2==0

check_even(8)

name = 'this is a global string'

def greet():
    name = 'sam'
    
    def hello():
        print('Hello' +name)
        
    hello()

greet()

x = int(input())
x

#returns the volume of a sphere

def vsphere():
    r = int(input())
    v = ( 4 / 3 ) * 3.14 * r**3
    return v
    vsphere()

# In[ ]:




