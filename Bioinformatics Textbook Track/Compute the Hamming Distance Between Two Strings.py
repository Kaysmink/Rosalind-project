# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 18:04:02 2018

@author: kaysm
"""

Input=open("Compute the Hamming Distance Between Two Strings.txt", "r") 
Input=Input.read().split("\n")
String1=Input[0]
String2=Input[1]

def hamming(pattern, text):
    count=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            count=count+1
    return count

print(hamming(String1, String2))
