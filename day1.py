#!/usr/bin/env python
# coding: utf-8

# In[1]:


#logical operators
a=7 


# In[2]:


b=8


# In[3]:


a>b


# In[4]:


a==b


# In[5]:


a<b


# In[6]:


a!=b


# In[7]:


1 < 2 < 3


# In[8]:


1 < 2 > 3


# In[9]:


1 < 2 and 2 < 3


# In[10]:


1 < 2 and 2 == 3


# In[11]:


1 < 2 or 2 == 3


# In[12]:


not 1 < 2


# In[13]:


not 1 == 9836487324


# In[14]:


#if else statements
if 3 > 4:
    a = 7
else:
    a = 8
    


# In[15]:


a


# In[16]:


if 2 + 9 == 10:
    b = 1
elif 8 + 10 == 98:
    b = 2
else:
    b = 3
    


# In[17]:


b


# In[18]:


dep = False

if dep:
    print('nutella')
else:
    print('peanut butter')


# In[19]:


a=0
i = 0
    


# In[20]:


#loops

while i<6:
    a = a + 1
    i = i + 1


# In[21]:


a


# In[22]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[23]:



for num in mylist:
    if num % 2 == 0:
        print('gelatin')
    else:
        print('jelly')


# In[24]:


list_sum = 2


# In[25]:


for num in mylist:
        list_sum = list_sum * num


# In[26]:


list_sum


# In[27]:


x = 0


# In[28]:


while x < 8:
    print(f'X is now equal to {x}')
    x += 1


# In[29]:


mylist = [1,2,3,4,5,6]


# In[30]:


for num in range(3,10,2):
    print(num)


# In[31]:


list(range(2,10,2))


# In[32]:


count = 0


# In[33]:



word = 'absde'
    


# In[34]:


for item,letter in enumerate(word):
    print(item)
    print(letter)


# In[35]:


list1 = [1,2,3,4,5]


# In[ ]:





# In[36]:


list2 = ['a','b','c']


# In[37]:


for item in zip(list1,list2):
    print(item)


# In[38]:


#gives new functions
from random import shuffle 


# In[39]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[40]:


shuffle(mylist)


# myist

# In[41]:


mylist


# In[42]:


mylist


# In[43]:


from random import randint


# In[44]:


randint(1,100)


# In[51]:


mynum = randint(0,100)


# In[52]:


mynum


# In[53]:


input('Enter a number here: ')


# In[54]:


inp = input('Enter your donuts: ')


# In[55]:


inp


# In[56]:


type(inp)


# In[59]:


inp = int(inp)


# In[60]:


inp


# In[13]:


mylist = [1,2,3,4,5,6,7,8,9]


# In[9]:


mylist.pop()


# In[10]:


mylist


# In[11]:


mylist.clear()


# In[14]:


mylist


# In[17]:


mylist.insert(0,9)


# In[21]:


string = 'shaheem is fat'


# In[22]:


mylist = [letter for letter in string]


# In[23]:


mylist


# In[24]:


sample = [1,2,3,4,5,6,7,8,9,10]


# In[29]:


mylist = [letter**2 for letter in sample if letter%2==0]


# In[30]:


mylist


# In[31]:


celsius = [10,20,24,27,30.5]


# In[32]:


far = [((9/5)*t + 32) for t in celsius]


# In[33]:


far


# In[38]:


sam = [1,2,3,4,5,6,7,8,9,10]


# In[39]:


result = [x if x%2==0 else 'ODD' for x in sam]


# In[40]:


result


# In[43]:


mylist = []

for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)


# In[44]:


mylist


# In[1]:


st = 'Print only the words that start with s in this sentence'
y=0
st[y+1]


# In[18]:


st = 'Print only the words that start with s in this sentence'


# In[19]:


fo = st.split()


# In[20]:


fo


# In[23]:


for x in fo:
    if x[0] == 's':
        print(x)


# In[1]:


f = range(1,10)


# In[2]:


f


# In[4]:


for num in range (1,11):
    if num%2 == 0:
        print(num)


# In[5]:


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


# In[6]:


for num in range(1,101):
    if num%15 == 0:
        print('FizzBuzz')
    elif num%5 == 0:
        print('Buzz')
    elif num%3 == 0:
        print('Fizz')
    else:
        print(num)


# In[7]:


st = 'Create a list of the first letters of every word in this string' #list comprehensions


# In[21]:


mylist = st.split()


# In[22]:


mylist


# In[26]:


[x[0] for x in mylist]


# In[27]:





# In[1]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[2]:


mylist.reverse()


# In[3]:


mylist


# In[5]:


f = mylist.copy()


# In[6]:


f


# In[25]:


def shaheem(a,b):
    return a-b


# In[26]:


shaheem(2,3)


# In[30]:


def hello(name='default'):
    print(f'Hello {name}')


# In[32]:



hello()


# In[35]:


21 % 2 == 0


# In[1]:


def eve_check(n):
    return n%2==0


# In[2]:


eve_check(21)


# In[7]:


def eve_check_list(lis):
    
    eve = []
    for num in lis:
        if num%2 == 0:
            eve.append(num)
        else:
            pass
    return eve


# In[8]:


mylist=[1,2,6,1,5,8,45,2,7,34]


# In[9]:


eve_check_list(mylist)


# In[ ]:




