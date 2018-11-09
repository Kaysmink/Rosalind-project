# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 18:42:45 2018

@author: kaysm
"""

Input=open("Find the Reverse Complement of a String.txt", "r") 
Input=Input.read()

length=len(Input)

Complement=""

for i in range(0,length):
     if(Input[i]=="A"):
         Complement=Complement+"T"
     if(Input[i]=="T"):
         Complement=Complement+"A"
     if(Input[i]=="C"):
         Complement=Complement+"G"
     if(Input[i]=="G"):
         Complement=Complement+"C"

Reverse=Complement[::-1]
print(Reverse)
