#!/usr/bin/env python
# coding: utf-8
def calc(a, b, op):

    if op not in '+-/*':
        return 'Please only type one of these characters: "+, -, *, /"'

    if op == '+':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
    if op == '-':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
    if op == '*':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
    if op == '/':
        return(str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
op = input('What kind of operation would you like to do?\\nChoose between "+, -, *, /" : ')

print(calc(a, b, op))




