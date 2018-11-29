# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:37:22 2018

@author: kaysm
"""
from Bio.Seq import Seq
import math

Input=open("rosalind_pmch.txt", "r") 
Input=Input.read().strip().split("\n")

seq=""
for i in range(1,len(Input)):
    seq=seq+Input[i]
    
seq=Seq(seq)

print(math.factorial(seq.count("A")) * math.factorial(seq.count("C")))