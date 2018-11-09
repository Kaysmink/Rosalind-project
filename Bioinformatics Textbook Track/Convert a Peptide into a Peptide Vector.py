# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 17:28:49 2018

@author: kaysm
"""

Input=open("rosalind_ba11c.txt", "r") 
Input=Input.read().split("\n")[0]
Input=[c for c in Input]


weights = [71,103,115,129,147,57,137,113,128,113,131,114,97,128,156,87,101,99,186,163]
acid=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

Index=acid.index(Input[0])
wommWeights=[weights[Index]]

for i in range(1,len(Input)):
    Index=acid.index(Input[i])
    W=wommWeights[i-1]+weights[Index]
    wommWeights.append(W)

string=""
for i in range(1,wommWeights[len(wommWeights)-1]+1):
    if(i in wommWeights):
        string=string+" 1"
    else:
        string=string+" 0"

print(string[1:])


    