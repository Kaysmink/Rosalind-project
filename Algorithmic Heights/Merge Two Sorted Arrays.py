# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:10:51 2018

@author: kaysm
"""

Input=open("Merge Two Sorted Arrays.txt", "r") 
Input=Input.read().split("\n")

N=[]
for i in range(0,len(Input)-1,2):
    N.append(int(Input[i]))
    
Numbers=[]

for i in range(0,len(Input)):
    if(i%2==1):
        Numbers.append(list(map(int,(Input[i]).split(" "))))

AllNumbers=[]

for i in range(0,len(Numbers)):
    for j in range(0,len(Numbers[i])):
        AllNumbers.append(Numbers[i][j])
        
AllNumbers.sort()

outputString=str(AllNumbers[0])
for i in range(1,len(AllNumbers)):
    outputString=outputString+" "+ str(AllNumbers[i])
    
print(outputString)

