# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 20:45:02 2018

@author: kaysm
"""

Input=open("Double-Degree Array.txt", "r") 
Input=Input.read().split("\n")

N=Input[0].split(" ")[0]
M=Input[0].split(" ")[1]

From=[]
To=[]
Degree=[]
DegreeOfNeigbor=[]

for i in range(1,int(M)+1):
    num=Input[i].split(" ")
    From.append(int(num[0]))
    To.append(int(num[1]))    
    
for i in range(1,int(N)+1):
    Degree.append(From.count(i)+To.count(i))

for i in range(1,int(N)+1):
    count=0
    for j in range(0,len(From)):
        if(From[j]==i):
            Neigbor=To[j]
            count=count+Degree[Neigbor-1]
        if(To[j]==i):
            Neigbor=From[j]
            count=count+Degree[Neigbor-1]
    DegreeOfNeigbor.append(count)

outputString=str(DegreeOfNeigbor[0])
for i in range(1,len(DegreeOfNeigbor)):
    outputString=outputString+" "+ str(DegreeOfNeigbor[i])
    
print(outputString)
