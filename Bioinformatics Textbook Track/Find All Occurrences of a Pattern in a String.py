# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:47:42 2018

@author: kaysm
"""

Input=open("Find All Occurrences of a Pattern in a String.txt", "r") 
Input=Input.read().split("\n")

String=Input[1]
SubString=Input[0]
indexes=[]

for i in range(0,len(String)-len(SubString)):
    if(SubString==String[i:i+len(SubString)]):
        indexes.append(i)
    
output=str(indexes[0])
for i in range(1,len(indexes)):
    output=output+" " + str(indexes[i])

print(output)
