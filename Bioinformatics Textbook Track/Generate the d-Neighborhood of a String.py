# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:51:31 2018

@author: kaysm
"""
import itertools as it
Input=open("Generate the d-Neighborhood of a String.txt", "r") 
Input=Input.read().split("\n")
Pattern=tuple(Input[0])
K=int(Input[1])

Letters = "ACGT"

def hamming(pattern, text):
    count=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            count=count+1
    return count

results=[]

f = open('Generate the d-Neighborhood of a String Output .txt','w')

for pattern in it.product(Letters, repeat=len(Pattern)):
    if(hamming(Pattern,pattern)<=K):
        results.append(pattern)
        string=pattern[0]
        for i in range(1,len(pattern)):
            string=string+pattern[i]
        f.write(string+"\n")
        
print("The output file has been written succesfully:\nCheck the file path dictionary")