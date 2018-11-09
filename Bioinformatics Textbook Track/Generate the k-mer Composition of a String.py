# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:39:17 2018

@author: kaysm
"""

Input=open("Generate the k-mer Composition of a String.txt", "r") 
Input=Input.read().split("\n")
K=int(Input[0])
Tekst=Input[1]

f = open('Generate the k-mer Composition of a String Output.txt','w')

for i in range(0,len(Tekst)-K+1):
    kMer=Tekst[i:i+K]
    f.write(kMer+"\n")

print("The output file has been written succesfully:\nCheck the file path dictionary")