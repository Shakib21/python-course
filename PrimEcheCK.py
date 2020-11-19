#!/usr/bin/env python
# coding: utf-8
def checkprime(n):
    for i in range(2,round(n/2)):
        if n%i == 0:
            return False
    return True

checkprime(3)