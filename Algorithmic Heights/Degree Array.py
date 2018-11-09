# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 20:10:28 2018

@author: kaysm
"""

Input=open("Degree Array.txt", "r") 
Input=Input.read().split("\n")

N=Input[0].split(" ")[0]
M=Input[0].split(" ")[1]

numbers=[]
Degree=[]

for i in range(1,int(M)+1):
    num=Input[i].split(" ")
    for j in range(0,len(num)):
        numbers.append(num[j])
        
numbers=[int(i) for i in numbers]

for i in range(1,int(N)+1):
    Degree.append(numbers.count(i))
    
outputString=str(Degree[0])

for i in range(1,len(Degree)):
    outputString=outputString+" "+ str(Degree[i])
    
print(outputString)

