# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:24:32 2018

@author: kaysm
"""

Input=open("Convert a Peptide Vector into a Peptide.txt", "r") 
Input=Input.read().split("\n")[0]
Input=Input.split(" ")

weights = [71,103,115,129,147,57,137,113,128,113,131,114,97,128,156,87,101,99,186,163]
acid=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

indexes=[]
masses=[]

for i in range(0,len(Input)):
    if(Input[i]=="1"):
        indexes.append(i+1)

masses=[indexes[0]]
  
result=""      
for i in range(1,len(indexes)):
    masses.append(indexes[i]-indexes[i-1])
    
for i in range(0,len(masses)):
    index=weights.index(masses[i])
    result=result+acid[index]
    
print(result)
        