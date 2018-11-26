# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:13:50 2018

@author: kaysm
"""
import itertools as it
import math

Input=open("Enumerating Gene Orders Output.txt", "r") 
N=int(Input.read())

listOfNumbers=list(range(1,N+1))
StringOfNumbers="".join(map(str,listOfNumbers))


f = open('Enumerating Gene Orders Output .txt','w')

f.write(str(math.factorial(N))+ "\n")
for pattern in it.permutations(StringOfNumbers):
    f.write(" ".join(pattern) + "\n" )