# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:25:13 2018

@author: kaysm
"""

Input=open("Variables and Some Arithmetic.txt", "r") 
Input=Input.read().split(" ")

value=int(Input[0])**2+int(Input[1])**2

print(value)