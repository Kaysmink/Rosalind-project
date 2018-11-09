# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:45:22 2018

@author: kaysm
"""
Input=open("Construct the Graph of a Spectrum.txt", "r") 
Input=Input.read().split("\n")
Input=Input[0].split(" ")
Input=list(map(int,Input))

weights = [71,103,115,129,147,57,137,113,128,113,131,114,97,128,156,87,101,99,186,163]
acid=['A','C','D','E','F','G','H','L','K','L','M','N','P','Q','R','S','T','V','W','Y']

for i in range(0,len(Input)):
    if(Input[i] in weights):
        Index=weights.index(Input[i])
        print("0->{}:{}".format(Input[i],acid[Index]))

for i in range(0,len(Input)):
    mass=Input[i]
    for j in range(i+1,len(Input)):
        value=Input[j]-mass
        if(value in weights):
            Index=weights.index(value)
            print("{}->{}:{}".format(mass,Input[j],acid[Index]))
            
    
