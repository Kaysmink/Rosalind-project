# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 13:20:31 2019

@author: kaysm
"""

Input=open("Find a Position in a Genome Minimizing the Skew.txt", "r") 
sequence=Input.read().split("\n")[0]

currentSkew=0
skewList=[currentSkew]

for i in range(0, len(sequence)):
    if(sequence[i]=="C"):
        currentSkew=currentSkew-1
    if(sequence[i]=="G"):
        currentSkew=currentSkew+1
    skewList.append(currentSkew)
    
minSkew=min(skewList)
indices = [i for i, x in enumerate(skewList) if x == minSkew]

print(" ".join(map(str,indices)))

    
    





