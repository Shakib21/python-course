#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#lambda functions

square = lambda num: num**2


# In[ ]:


mynums = [9,9]


# In[ ]:


list(map(lambda num: num**2,mynums))


# In[ ]:





# In[ ]:


check_even = lambda num: num%2==0


# In[ ]:


check_even(8)


# In[ ]:


name = 'this is a global string'

def greet():
    name = 'sam'
    
    def hello():
        print('Hello' +name)
        
    hello()

greet()


# In[ ]:


x = int(input())


# In[ ]:


x


# In[ ]:


def vsphere():
    r = int(input())
    v = ( 4 / 3 ) * 3.14 * r**3
    return v
    


# In[ ]:


vsphere()


# In[ ]:




