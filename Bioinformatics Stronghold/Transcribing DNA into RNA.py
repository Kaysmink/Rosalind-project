# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:27:53 2018

@author: kaysm
"""

Input=open("Transcribing DNA into RNA.txt", "r") 
Input=Input.read()

RNA=""

length=len(Input)

for i in range(0,length):
    if(Input[i]=="T"):
        RNA=RNA+"U"
    else:        
        RNA=RNA+Input[i]

print(RNA)
    
