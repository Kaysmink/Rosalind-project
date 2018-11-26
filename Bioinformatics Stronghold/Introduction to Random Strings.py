# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:22:48 2018

@author: kaysm
"""
import math

Input=open("Introduction to Random Strings.txt", "r") 
Input=Input.read().split("\n")
String=Input[0]
GcContents=list(map(float,Input[1].split(" ")))

Prob=[]
for i in range(0,len(GcContents)):
    GC=GcContents[i]/2
    AT=(1-GC*2)/2
    ratioDict={"A":AT, "C":GC, "G":GC, "T":AT}
    
    P=1
    for j in range(0,len(String)):
        P=P*ratioDict[String[j]]
    
    Prob.append(round(math.log(P,10),3))

Prob=list(map(str,Prob))   
print(" ".join(Prob))
        
    
    

