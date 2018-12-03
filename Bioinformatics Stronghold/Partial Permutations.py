# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 12:25:17 2018

@author: kaysm
"""

import math

Input=open("Partial Permutations.txt", "r") 
Input=Input.read().strip().split(" ")
N=int(Input[0])
K=int(Input[1])

answer=(math.factorial(N)/(math.factorial(N-K)))%1000000

print(int(answer))