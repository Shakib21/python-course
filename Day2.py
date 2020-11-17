#!/usr/bin/env python
# coding: utf-8

# In[1]:


#work hours done by employees

workhours = [('Johann',100),('Ben',200),('Anant',300)]


# In[2]:


#employee of the highest salary

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


# In[3]:


eotf(workhours)


# In[ ]:


#shuffle function

ex = [1,2,3,4,5,6,7]


# In[ ]:



from random import shuffle


# In[ ]:


shuffle(ex)


# In[ ]:


ex


# In[ ]:


#shuffles the list

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
    


# In[ ]:


result = shuffle_list(ex)


# In[ ]:



result


# In[ ]:



#guessing game

mylist = ['','O','']


# In[ ]:


shuffle_list(mylist)


# In[ ]:



def player_guess():
    guess=''
    
    while guess not in ['0','1','2']:
        
        guess = input("Pink a number 0,1,2")
    
    return int(guess)

    


# In[ ]:


player_guess()


# In[ ]:


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct!')
    else:
        print('wrong guess :(')
        print(mylist)
        


# In[ ]:


#initial list
mylist = [' ','O',' ']

#SHUFFLE LIST
mixeduplist = shuffle_list(mylist)

#USER GUESS
guess = player_guess()

#CHECK GUESS
check_guess(mixeduplist,guess)


# In[ ]:


#args

def myfunc(*args):
    #returns 5% of the sum of a and b
    return sum(args) * 0.05
    


# In[ ]:


myfunc(40,60,100,200,900,758,42,98,2,20)


# In[ ]:


#kwargs

def func(**kwargs):
    if 'jojo' in kwargs:
        print('My jojo of choice is {}'.format(kwargs['jojo']))
    else:
        print('I did not find any fruit here')
    


# In[ ]:




func(jojo = 'johnny joestar',veggie = 'lettuce')


# In[ ]:


#game: if the number 007 comes in that right order, return True

def spy_game(mylist):
    
    code = [0,0,7,'x']
    
    for n in mylist:
        if n == code[0]:
            code.pop(0)
    
    return len(code) == 1
    


# In[ ]:


spy_game([1,3,4,0,7,7,0])


# In[ ]:


def square(num):
    return num**2
    


# In[ ]:


nums = [1,2,3,4,5]


# In[ ]:


list(map(square,nums))
 


# In[ ]:


#returns the even number

def splicer(mystring):
    if len(mystring)%2==0:
        return 'Even'
    else:
        return mystring[0]
        


# In[ ]:


name = ['Ant','Jozu','Hayyan']


# In[ ]:


list(map(splicer,name))


# In[ ]:




