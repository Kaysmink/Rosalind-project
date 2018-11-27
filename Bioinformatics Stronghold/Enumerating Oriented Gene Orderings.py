# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:19:33 2018

@author: kaysm
"""

import itertools as it

Input=open("rosalind_sign.txt", "r") 
N=int(Input.read())

listOfNumbers=[i for i in range(-N,N+1) if i!=0]

f = open('Enumerating Oriented Gene Orders Output.txt','w')    

Count=0
for pattern in it.permutations(listOfNumbers,N):
    stop=0
    for number in pattern:
        if(-number in pattern):
            stop=1
            break
    if(stop==0):
        Count=Count+1
        f.write(" ".join(str(i) for i in pattern) + "\n")
print(Count)