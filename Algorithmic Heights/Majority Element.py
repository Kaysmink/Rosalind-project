# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:49:02 2018

@author: kaysm
"""

Input=open("Majority Element.txt", "r") 
Input=Input.read().split("\n")

K=int(Input[0].split(" ")[0])
N=int(Input[0].split(" ")[1])

for i in range(0,K+1):
    Input[i]=Input[i].split(" ")
    Input[i]=list(map(int,  Input[i]))

ListOfSequences=Input[1:K+1]
Results=[[]]*K

for i in range(0,K):
    amount=0
    num=-1
    for j in range(0,max(ListOfSequences[i])+1):
        if(ListOfSequences[i].count(j)>amount):
            amount=ListOfSequences[i].count(j)     
        if(amount>N/2):
            num=j
            break
    Results[i].append(num)
    
outputString=str(Results[0][0])
for i in range(1,len(Results[0])):
    outputString=outputString+" "+ str(Results[0][i])
    
print(outputString)
        
