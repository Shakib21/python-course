#!/usr/bin/env python
# coding: utf-8
import requests
import bs4

#a sample site to scrape details from as to avoid copywrite issues

'https://books.toscrape.com/catalogue/page-2.html'

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')
products =soup.select(".product_pod")
example = products[0]
example
example.select(".star-rating.Three")
example.select('a')[1]['title']
two_star = []

for n in range(1,51):
    
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        
        if len(book.select('.star-rating-Two')) !=0:
            book_title = example.select('a')[1]['title']
            two_star.append(book_title)
            
            two_star

from PIL import Image

 import smtplib
 smtp_ob = smtplib.SMTP('smtp.gmail.com',587)
smtp_ob.ehlo()
smtp_ob.starttls()
password = input('What is your password: ')
import getpass
password = getpass.getpass('Pass pls: ')

#Advanced Functions


 hex(512)
 
hex(1024)
bin(512)
bin(7)
pow(2,3)
pow(8,7)
abs(-987654)
round(4.6)
round(6.45678987654,2)
s = 'hello world'
s.capitalize()
s.lower()
s.count('o')
s.find('o')
s
s.center(20,'z')
s.isalnum()
s.islower()
s.istitle()
s = 'hello'
s.partition('e')
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
def func(x):
    return x
    interact(func,x='Hello')
def g(x,y):
    return(x,y)
    @interact(x=True,y=1.0)
def g(x,y):
    return(x,y)
    interact(func,x=widgets.IntSlider(min=0,max=100,step=1,value=50))
interact(func,x=(-100,100,1))
interact(func,x=['helo','akjbcsajdhb','hi'])
from IPython.display import display
def f(a,b):
    display(a+b)
    return a+b
    w = interactive(f,a=10,b=20)
w.children
display(w)


