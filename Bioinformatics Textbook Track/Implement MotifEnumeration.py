# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:14:39 2018

@author: kaysm
"""

import itertools as it

def hamming(pattern, text):
    count=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            count=count+1
    return count

Input=open("Implement MotifEnumeration.txt", "r") 
Input=Input.read().split("\n")
values=Input[0].split(" ")
K=int(values[0])
D=int(values[1])

Letters = "ACGT"
Results=[]

DnaStrings=[]
for i in range(1,len(Input)):
    DnaStrings.append(Input[i])

for pattern in it.product(Letters, repeat=K):
    count=0
    for i in range(0,len(DnaStrings)):
        string=DnaStrings[i]
        for j in range(0,len(DnaStrings[i])-K+1):
            Tekst=string[j:j+K]
            if(hamming(pattern, Tekst)<=D):
                count=count+1
                break
    if(count==len(DnaStrings)-1):
        toAdd=pattern[0]
        for i in range(1,len(pattern)):
            toAdd=toAdd+pattern[i]
        Results.append(toAdd)

answer=Results[0]

for i in range(1,len(Results)):
    answer=answer+" "+Results[i]

print(answer)        





                
            
            
            
            
            
            
            
            
            

