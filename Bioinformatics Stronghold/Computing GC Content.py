# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:45:29 2018

@author: kaysm
"""
def num_there(s):
    return any(i.isdigit() for i in s)

Input=open("Computing GC Content.txt", "r") 
Input=Input.read().split()

Names=[]
Dna=[]

highest=0
index=0

for i in range(0,len(Input)):
    if(">"in Input[i]):
        Names.append(Input[i])        
        
i=1
while(i < len(Input)):
    dnaString=""
    while(num_there(Input[i])==False):
        dnaString=dnaString+Input[i]
        i=i+1
        if(i==len(Input)):
            break       
    
    Dna.append(dnaString)
    i=i+1

GCContent=[0]*len(Names)

for i in range(0,len(Dna)):
    length=len(Dna[i])
    NumOfCG=Dna[i].count("C")+Dna[i].count("G")
    GCContent[i]=NumOfCG/length
    
    if(GCContent[i]>highest):
        highest=GCContent[i]
        index=i
        
print(Names[index][1:])
print(GCContent[index]*100)

    