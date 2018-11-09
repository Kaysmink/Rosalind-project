# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 16:58:01 2018

@author: kaysm
"""

import numpy as np

def num_there(s):
    return any(i.isdigit() for i in s)

Input=open("Consensus and Profile.txt", "r") 
Input=Input.read().split("\n")

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

matrix=np.matrix(Dna)
A=[]
C=[]
G=[]
T=[]
MostOccurs=[]

for i in range(len(Dna[0])):
    NumA=0
    NumC=0
    NumG=0
    NumT=0
    
    x=matrix[:,i].tolist()
    string=''.join(x[0])
    for i in range(1,len(x)): 
        string=string + str(x[i][0])
    
    A.append(string.count("A"))
    C.append(string.count("C"))
    G.append(string.count("G"))
    T.append(string.count("T"))

for i in range(0,len(Dna[0])):
    high=0
    most=""
    
    if(A[i]>high):
        high=A[i]
        most="A"
    if(C[i]>high):
        high=C[i]
        most="C"
    if(G[i]>high):
        high=G[i]
        most="G"
    if(T[i]>high):
        high=T[i]
        most="T"
    MostOccurs.append(most)

StringMost=""
StringA="A:"
StringC="C:"
StringG="G:"
StringT="T:"

for i in range(0,len(MostOccurs)):
    StringMost=StringMost+MostOccurs[i]
    StringA=StringA+" "+str(A[i])
    StringC=StringC+" "+str(C[i])
    StringG=StringG+" "+str(G[i])
    StringT=StringT+" "+str(T[i])

print(StringMost)
print(StringA)
print(StringC)
print(StringG)
print(StringT)



    
        
        
        
        
        
        
        
        
        

