# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:13:10 2018

@author: kaysm
"""

Input=open("Counting DNA Nucleotides.txt", "r") 
Input=Input.read()

letters=[]
length=len(Input)

AmountA=0
AmountC=0
AmountG=0
AmountT=0

for i in range(0,length):
    if(Input[i]=="A"):
        AmountA=AmountA+1
    if(Input[i]=="C"):
        AmountC=AmountC+1
    if(Input[i]=="G"):
        AmountG=AmountG+1
    if(Input[i]=="T"):
        AmountT=AmountT+1


print(AmountA, AmountC, AmountG, AmountT)
    
    
    