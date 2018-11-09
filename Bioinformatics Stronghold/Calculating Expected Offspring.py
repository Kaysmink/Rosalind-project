# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 14:59:36 2018

@author: kaysm
"""

Input=open("Calculating Expected Offspring.txt", "r") 
Input=Input.read().split(" ")

AAAA=1
AAAa=1
AAaa=1
AaAa=3/4
Aaaa=1/2
aaaa=0

amount=2*AAAA*int(Input[0])+2*AAAa*int(Input[1])+2*AAaa*int(Input[2])+2*AaAa*int(Input[3])+2*Aaaa*int(Input[4])+2*aaaa*int(Input[5])
print(amount)
