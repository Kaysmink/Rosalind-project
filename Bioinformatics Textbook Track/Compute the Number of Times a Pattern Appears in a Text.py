# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:45:42 2018

@author: kaysm
"""

Input=open("Compute the Number of Times a Pattern Appears in a Text.txt", "r") 
Input=Input.read().split("\n")
Text=Input[0]
Pattern=Input[1]

def patternCount(text,pattern):    
    count=0    
    for i in range(0,len(text)-len(pattern)+1):
        if(pattern==text[i:i+len(pattern)]):
            count=count+1
    return count
        
print(patternCount(Text,Pattern))