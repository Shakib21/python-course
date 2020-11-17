#!/usr/bin/env python
# coding: utf-8
workhours = [('Johann',100),('Ben',200),('Anant',300)]
def eotf(wh):
    current_max = 0
    eotm = ''
    
    for e,h in wh:
        if h>current_max:
            current_max=h
            eotm = e
        else:
            pass
    return(eotm,current_max)
eotf(workhours)
ex = [1,2,3,4,5,6,7]
from random import shuffle
shuffle(ex)
ex
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    result = shuffle_list(ex)

result
mylist = ['','O','']
shuffle_list(mylist)
def player_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        
        guess = input("Pink a number 0,1,2")
    
    return int(guess)

    player_guess()
def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('wrong guess :(')
        print(mylist)
        #initial list
mylist = [' ','O',' ']

#SHUFFLE LIST
mixeduplist = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixeduplist,guess)

def myfunc(*args):
    #returns 5% of the sum of a and b
    return sum(args) * 0.05
    myfunc(40,60,100,200,900,758,42,98,2,20)

def func(**kwargs):
    if 'jojo' in kwargs:
        print('My jojo of choice is {}'.format(kwargs['jojo']))
    else:
        print('I did not find any fruit here')
    func(jojo = 'johnny joestar',veggie = 'lettuce')

def spy_game(mylist):
    
    code = [0,0,7,'x']
    
    for n in mylist:
        if n == code[0]:
            code.pop(0)
    
    return len(code) == 1
    spy_game([1,3,4,0,7,7,0])
def square(num):
    return num**2
    nums = [1,2,3,4,5]
list(map(square,nums))
 def splicer(mystring):
    if len(mystring)%2==0:
        return 'Even'
    else:
        return mystring[0]
        name = ['Ant','Jozu','Hayyan']
list(map(splicer,name))





