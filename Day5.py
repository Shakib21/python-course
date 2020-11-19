#!/usr/bin/env python
# coding: utf-8
class Dog():
    species = 'mammal'
    
    def __init__(self,mybreed,name,spots):
        
        self.breed = mybreed
        self.name = name
        self.spots = spots
        
    def bark(self,food):
        
        print('WOOF! My name is {} and I like {}'.format(self.name,food))
        my_dog = Dog('Golden Retriever','goldie',False,)
ryans_dog = Dog(mybreed='Huskie',name='Marley',spots=True)
my_dog.name
my_dog.bark('treats')
class Circle():
    
    pi = 3.14
    
    def __init__(self,radius=1):
        self.r = radius
        
    def circumference(self):
        return self.r * self.pi * 2
    
    def area(self):
        return self.r * self.r * self.pi
circ = Circle(7)
circ.pi
circ.r
circ.circumference()
class Dog():
    species = 'mammal'
    
    def __init__(self,mybreed,name,spots):
        
        self.breed = mybreed
        self.name = name
        self.spots = spots
        
    def bark(self,food):
        
        print('WOOF! My name is {} and I like {}'.format(self.name,food))
        class Animal():
    
    def __init__(self):
        print('Animal created')
    def who_am_i(self):
        print('I am an Animal')
    def eat(self):
        print('I am eating')
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        
        print('Dog Created')
        
    def who_am_i(self):
        print('I am a dog!')
        mydog = Dog()

mydog.who_am_i()
mydog.eat()

mydog.__init__()class Book():
    def __init__(self,title,author,pages):
        
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        
        return self.pages
    
    def __del__(self):
        
        print("A book object has been deleted")
        b = Book('Percy Jackson','Rick Riordan', 290)
print(b)
del (b)

# In[31]:





# In[ ]:




