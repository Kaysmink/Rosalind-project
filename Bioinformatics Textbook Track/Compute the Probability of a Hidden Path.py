# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 15:33:34 2018

@author: kaysm
"""
import numpy as np

Input=open("Compute the Probability of a Hidden Path.txt", "r") 
Input=Input.read().split("\n")

path=Input[0]
pathList=[c for c in path]

for i in range(0,len(pathList)):
    if(pathList[i]=="A"):
        pathList[i]=0
    if(pathList[i]=="B"):
        pathList[i]=1

P=0.5
old=pathList[0]

pAA=float(Input[5].split("\t")[1])
pAB=float(Input[5].split("\t")[2])
pBA=float(Input[6].split("\t")[1])
pBB=float(Input[6].split("\t")[2])

matrix = np.array([[pAA,pAB],[pBA,pBB]])

for i in range(1,len(pathList)):
    new=pathList[i]
    P=P*matrix[old][new]
    old=new
    
print(P)

    
    
    


