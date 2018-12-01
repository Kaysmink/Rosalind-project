# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 21:15:35 2018

@author: kaysm
"""

import itertools as it

Input=open("Ordering Strings of Varying Length Lexicographically.txt", "r") 
Input=Input.read().strip().split("\n")
Symbols="".join(Input[0].split(" "))
N=int(Input[1])

f = open('Ordering Strings of Varying Length Lexicographically Output.txt','w')

List=[]
for i in range(1,N+1):
    for pattern in it.product(Symbols,repeat=i):
        List.append("".join(pattern))
        
List=(sorted(List, key=lambda word: [Symbols.index(c) for c in word]))

f.write("\n".join(List))
        



