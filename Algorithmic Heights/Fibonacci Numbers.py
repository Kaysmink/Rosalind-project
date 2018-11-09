# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 19:35:08 2018

@author: kaysm
"""

Input=open("Fibonacci Numbers.txt", "r") 
Input=Input.read()
N=int(Input)

Numbers=[]
for i in range(0,2):
    Numbers.append(1)    

for i in range(2,N):
    Numbers.append(Numbers[i-2]+Numbers[i-1])

print(Numbers[len(Numbers)-1])