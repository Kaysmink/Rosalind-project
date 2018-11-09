# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:16:54 2018

@author: kaysm
"""
import numpy as np

Input=open("Compute the Probability of an Outcome Given a Hidden Path.txt", "r") 
Input=Input.read().split("\n")

pathXY=Input[0]
path=Input[4]
pathXY=[c for c in pathXY]
path=[c for c in path]

for i in range(0,len(pathXY)):
    if(pathXY[i]=="x"):
        pathXY[i]=0
    if(pathXY[i]=="y"):
        pathXY[i]=1
    if(pathXY[i]=="z"):
        pathXY[i]=2
        
for i in range(0,len(path)):
    if(path[i]=="A"):
        path[i]=0
    if(path[i]=="B"):
        path[i]=1

pAX=float(Input[9].split("\t")[1])
pAY=float(Input[9].split("\t")[2])
pAZ=float(Input[9].split("\t")[3])
pBX=float(Input[10].split("\t")[1])
pBY=float(Input[10].split("\t")[2])
pBZ=float(Input[10].split("\t")[3])

matrix = np.array([[pAX,pAY,pAZ],[pBX,pBY,pBZ]])

P=1

for i in range(0,len(path)):
    P=P*matrix[path[i]][pathXY[i]]

print(P)
    
    
    
