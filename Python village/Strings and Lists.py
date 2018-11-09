# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:30:58 2018

@author: kaysm
"""

Input=open("Strings and Lists.txt", "r") 
Input=Input.read().split("\n")
index=Input[1].split(" ")
String=Input[0]

(a,b,c,d)=int(index[0]),int(index[1]),int(index[2]),int(index[3])

word1=String[a:b+1]
word2=String[c:d+1]

print(word1, word2)