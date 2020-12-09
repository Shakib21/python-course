#!/usr/bin/env python
# coding: utf-8
##Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide 
##it by 2. If n is odd, multiply it by 3 and add 1

def func(n):
    
    num = n
    i=0
    while(num>1):
        if num%2==0:
            num/=2
        else:
            num = (num*3) + 1
        i+=1
    print('Number of steps it took is %i' %i)
    ch = int(input("Enter your choice: "))

func(ch)
