# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:43:38 2018

@author: kaysm
"""
import numpy as np

def num_there(s):
    return any(i.isdigit() for i in s)

Input=open("Overlap Graphs.txt", "r") 
Input=Input.read().split("\n")


Names=[]

for i in range(0,len(Input)):
    if(">"in Input[i]):
        Names.append(Input[i][1:])        
     
Dna=[]
i=1
while(i < len(Input)):
    dnaString=""
    while(num_there(Input[i])==False):
        dnaString=dnaString+Input[i]
        i=i+1
        if(i==len(Input)):
            break       
    
    dnaString=list(dnaString)
    Dna.append(dnaString)
    
    i=i+1
    
s=(len(Names), len(Names))
matrix=np.zeros(s)

for i in range(0,len(Dna)):
    for j in range(0,len(Dna)):
        if(i!=j):
            stringI=Dna[i][0]+Dna[i][1]+Dna[i][2]
            stringJ=Dna[j][len(Dna[j])-3]+Dna[j][len(Dna[j])-2]+Dna[j][len(Dna[j])-1]
            
            if(stringI==stringJ):
                matrix[i,j]=1

for i in range(0,len(Dna)):
    for j in range(0,len(Dna)):
        if(matrix[i,j]==1):
            print(Names[j], Names[i])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
