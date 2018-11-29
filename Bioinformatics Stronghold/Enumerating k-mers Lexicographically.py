# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 14:05:31 2018

@author: kaysm
"""

import itertools as it

Input=open("rosalind_lexf.txt", "r") 
Input=Input.read().split("\n")
Symbols=Input[0].split(" ")
N=int(Input[1])

Symbols="".join(Symbols)

f = open('Enumerating k-mers Lexicographically Output.txt','w')

for pattern in it.product(Symbols,repeat=N):
    f.write("".join(pattern) + "\n")

    
