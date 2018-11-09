# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:40:15 2018

@author: kaysm
"""

Input=open("Conditions and Loops.txt", "r") 
Input=Input.read().split(" ")

a,b=int(Input[0]),int(Input[1])

Sum=0
for i in range(a,b+1):
        if(i%2==1):
            Sum=Sum+i
            
print(Sum)          