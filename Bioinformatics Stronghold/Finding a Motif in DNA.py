# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:15:13 2018

@author: kaysm
"""

Input=open("Finding a Motif in DNA.txt", "r") 
Input=Input.read().split("\n")

String=Input[0]
SubString=Input[1]
indexes=[]

for i in range(0,len(String)-len(SubString)):
    if(SubString==String[i:i+len(SubString)]):
        indexes.append(i+1)
    
output=str(indexes[0])
for i in range(1,len(indexes)):
    output=output+" " + str(indexes[i])

print(output)


