#!/usr/bin/env python
# coding: utf-8


def palindrome(str):
    
    s = len(str)
    
    for i in range(0,s-1):
        
        if str[i]!=str[s-i-1]:
            return False
        
    return True



mystr = 'racecar'

palindrome(mystr)




