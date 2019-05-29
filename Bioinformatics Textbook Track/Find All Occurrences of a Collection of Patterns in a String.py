# -*- coding: utf-8 -*-
"""
Created on Wed May 29 11:05:35 2019

@author: kaysm
"""
import re

Input=open("Find All Occurrences of a Collection of Patterns in a String.txt", "r") 
Input=Input.read().split("\n", 1)
Text=Input[0]
patterns=Input[1].split("\n")

result=[]

for pattern in patterns:
    indexes=[m.start() for m in re.finditer('(?=%s)'% pattern, Text)]
    for index in indexes:
        result.append(index)
        
result=list(map(str, result))
result.sort()
print(" ".join(result))

    
    
