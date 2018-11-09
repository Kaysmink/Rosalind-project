# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:43:15 2018

@author: kaysm
"""
import itertools as it

Input=open("Generate the Frequency Array of a String.txt", "r") 
Input=Input.read().split("\n")
Text=Input[0]
K=int(Input[1])

Letters = "ACGT"
combinations=list(it.product(Letters, repeat=K))
freqArray=[]

def patternCount(text,pattern):    
    count=0    
    for i in range(0,len(text)-len(pattern)+1):
        if(pattern==text[i:i+len(pattern)]):
            count=count+1
    return count

for i in range(0,len(combinations)):
    pattern=""
    for j in range(len(combinations[i])):
        pattern=pattern+combinations[i][j]
    combinations[i]=pattern

for i in range(0,len(combinations)):
    pattern=combinations[i]
    freqArray.append(patternCount(Text,pattern))

answer="{}".format(freqArray[0])

for i in range(1,len(freqArray)):
    answer=answer+ " {}".format(freqArray[i])
    
print(answer)









