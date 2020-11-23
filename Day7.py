#!/usr/bin/env python
# coding: utf-8



x = [1,2,3]
y=2
z=3
result = y+z
print(result)
result = x+y
result
import pdb
x = [1,2,3]
y = 2
z = 3

resulto = y+z
pdb.set_trace()
reultt = y+x

#helps identify phone numbers in text

text = 'my friends phone number is 055-123-4567'
'phone' in text
import re
match = re.search('phone',text)
match
match
pattern = 'NOT IN TEXT'
re.search(pattern,text)
pattern = 'phone'
match = re.search(pattern,text)
match
text = 'my phone once, my phone twice'
match = re.search('phone',text)
match
import finditer
text = 'my friends phone number is 55-123-4567'
phone = re.search(r'\d{2,3}-\d{3}-\d{4}',text)
phone.group()
phrase = 'There are 3 numbers 34 inside 5 this sentence'

pattern = r'[^\d]+'

re.findall(pattern,phrase)test_phrase = 'This is a string! but it has punctuation. How can we remove it?'

re.findall(r'[^!.? ]+',test_phrase)

text = 'Only find the hyphen-words in this sentence'

pattern = r'[\w]+-[\w]+'

re.findall(pattern,text)

text = 'Hello, would you like some catfish?'

pattern = r'cat+[\w]+'

re.findall(pattern,text)

def func(n):
    return list(map(str,range(n)))

func(6)

import time

start_time = time.time()
result = func(10000)
end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)


stmt = '''

def func(n):
    return [str(num) for num in range(n)]

'''

setup= '''

func(100)

'''

import timeit

timeit.timeit(setup,stmt,number=100000)

import zipfile
-

comp_file = zipfile.Zipfile('comp_file.zip','w')

import requests
import bs4

result = requests.get("http://example.com")

type(result)

result.text

import bs4

soup = bs4.BeautifulSoup(result.text,"lxml")

soup

soup.select('title')[0].getText()

site_para = soup.select("p")

site_para[0]

res = requests.get('http://en.wikipedia.org/wiki/Grace_Hopper')

soup = bs4.BeautifulSoup(res.text,"lxml")

first_item = soup.select('.toctext')[0]

first_item.text

for item in soup.select('.toctext'):
    print(item.text)
    res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.thumbimage')

comp = soup.select('.thumbimage')[0]

comp['src']

import requests

# 
