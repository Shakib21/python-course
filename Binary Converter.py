#!/usr/bin/env python
# coding: utf-8
def binaryconvert(n):
    
    num = n
    b=0
    while(num!=0):
    
        i=0
        
        while(2**i <= num):
            
            i+=1
        
        b+= 10**(i-1)
        
        num-=2**i
        
    
    print(num)

binaryconvert(7)

2**0


def convert(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2, end = '') 
    
    
dec = int(input('Enter: '))
convert(dec) 