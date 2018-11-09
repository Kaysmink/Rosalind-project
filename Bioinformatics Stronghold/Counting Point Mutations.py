# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:17:42 2018

@author: kaysm
"""

Input=open("Counting Point Mutations.txt", "r") 
Input=Input.read().split("\n")

numOfMutations=0

for i in range(0,len(Input[0])):
    if(Input[0][i]!=Input[1][i]):
        numOfMutations=numOfMutations+1
        
print(numOfMutations)
