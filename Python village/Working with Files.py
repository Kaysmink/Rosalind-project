# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:47:39 2018

@author: kaysm
"""

Input=open("Working with Files.txt", "r") 
Input=Input.read().split("\n")

for i in range(1,len(Input),2):
    print(Input[i])