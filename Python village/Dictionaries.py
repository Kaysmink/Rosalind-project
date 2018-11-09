# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:51:53 2018

@author: kaysm
"""

Input=open("Dictionaries.txt", "r") 
Input=Input.read().split("\n")
words=[]
amount=[]
allWords=Input[0].split(" ")

for word in Input[0].split(' '):
    x=word
    if(x not in words):
      words.append(x) 
      

for i in range(0,len(words)):
    value=0
    for j in range(0,len(allWords)):
        if(words[i]==allWords[j]):
            value=value+1
    amount.append(value)
    print(words[i],value)

