#!/usr/bin/env python
# coding: utf-8
import random

def flip():
    f = random.random()
    
    if(f<=0.5):
        return True
    else:
        return False


choice = int(input('PLease enter the number of flips you would like to do: '))

result = []
for i in range(1,choice+1):
    if(flip()):
        result.append('H')
    else:
        result.append('T')
print('Number of Heads is %i' %result.count("H"))
print('Number of Tails is %i' %result.count("T"))
print(result)