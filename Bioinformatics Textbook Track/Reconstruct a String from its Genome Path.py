# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 20:48:22 2018

@author: kaysm
"""

Input=open("Reconstruct a String from its Genome Path.txt", "r") 
Input=Input.read().split("\n")

Text=Input[0]

for i in range(1,len(Input)-1):
    Text=Text+Input[i][len(Input[i])-1]
    
print(Text)