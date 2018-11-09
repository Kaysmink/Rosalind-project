# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:37:04 2018

@author: kaysm
"""
import itertools as it

Input=open("Implement NumberToPattern.txt", "r") 
Input=Input.read().split("\n")
Number=int(Input[0])
K=int(Input[1])

Letters = "ACGT"

count=0
for pattern in it.product(Letters, repeat=K):
    if(count==Number):
        result=(list(pattern))        
        break
    count=count+1

string=result[0]

for i in range(1,len(result)):
    string=string+result[i]
    
print(string)
    
        