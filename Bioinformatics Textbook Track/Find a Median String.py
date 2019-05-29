# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:28:04 2019

@author: kaysm
"""

import itertools as it
Input=open("Find a Median String.txt", "r") 
Input=Input.read().split("\n")
k=int(Input[0])
Dna=Input[1:]

def hamming(pattern, text):
    distance=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            distance=distance+1
    return distance

min_distance=10000
result=""
pattern=[]

for comb in it.product(["A", "C", "T", "G"],repeat=k):
    comb="".join(comb)
    score=0
    for dna in Dna:
        min_p=10000
        for i in range(0,len(dna)-len(comb)+1):
            kmer=dna[i:i+len(comb)]
            p=hamming(comb, kmer)
            if(p<min_p):
                min_p=p
        score=score+min_p
    if(score<min_distance):
        min_distance=score
        result=comb
        
print(result)
        
    

