# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 19:01:01 2018

@author: kaysm
"""

Input=open("Find the Most Frequent Words in a String.txt", "r") 
Input=Input.read().split("\n")
Text=Input[0]
lenOfPattern=int(Input[1])

def patternCount(text,pattern):    
    count=0    
    for i in range(0,len(text)-len(pattern)+1):
        if(pattern==text[i:i+len(pattern)]):
            count=count+1
    return count

Patterns=[]
Num=[]
result=""

for i in range(0,len(Text)-lenOfPattern+1):
    Pattern=Text[i:i+lenOfPattern]    
    if(Pattern not in Patterns):
        Patterns.append(Pattern)
        Num.append(patternCount(Text,Pattern))

for i in range(0,len(Num)):
    if(Num[i]==max(Num)):
      result=result + Patterns[i] + " "  
      
print(result)