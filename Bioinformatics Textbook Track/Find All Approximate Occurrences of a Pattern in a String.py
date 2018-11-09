# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:11:34 2018

@author: kaysm
"""

Input=open("Find All Approximate Occurrences of a Pattern in a String.txt", "r") 
Input=Input.read().split("\n")
Pattern=Input[0]
Text=Input[1]
D=int(Input[2])

result=[]

def hamming(pattern, text):
    distance=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            distance=distance+1
    return distance

for i in range(0,len(Text)-len(Pattern)+1):
    text=Text[i:i+len(Pattern)]
    if (hamming(Pattern, text)<=D):
        result.append(i)

result=list(map(str,result))
answer=result[0]

for i in range(1,len(result)):
    answer=answer+ " "+result[i]
    
print(answer)
