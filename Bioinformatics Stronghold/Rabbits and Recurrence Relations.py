# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:01:56 2018

@author: kaysm
"""

Input=open("Rabbits and Recurrence Relations.txt", "r") 
Input=Input.read().split()

N=int(Input[0])
K=int(Input[1])

numOfOld=1
numOfYoung=0

for i in range(2,N):
    old=numOfOld
    young=numOfYoung
    
    numOfYoung=old*K
    numOfOld=old+young
    
NumOfPairs=numOfYoung + numOfOld
print(NumOfPairs)
    


