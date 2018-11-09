# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 19:43:11 2018

@author: kaysm
"""

Input=open("Binary Search.txt", "r") 
Input=Input.read().split("\n")

N=Input[0]
M=Input[1]

SortedArray=Input[2].split(" ")
RandomIntegers=Input[3].split(" ")
Indexes=[]

for i in range(0,len(RandomIntegers)):
    if(RandomIntegers[i] in SortedArray):
        Indexes.append(SortedArray.index(RandomIntegers[i])+1)
    else:
        Indexes.append(-1)
   
outputString=str(Indexes[0])

for i in range(1,len(Indexes)):
    outputString=outputString+" "+ str(Indexes[i])
        
print(outputString)