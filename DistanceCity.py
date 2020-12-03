#!/usr/bin/env python
# coding: utf-8
def distance_check(x,y,a,b):
    
    return (((x-a)**2) - ((y-b)**2))**(0.5)

caa = int(input('Please enter the X co-ordinates of the first city: '))
cab = int(input('Please enter the Y co-ordinates of the first city: '))
cba = int(input('Please enter the X co-ordinates of the second city: '))
cbb = int(input('Please enter the Y co-ordinates of the second city: '))

distance_check(caa,cab,cba,cbb)