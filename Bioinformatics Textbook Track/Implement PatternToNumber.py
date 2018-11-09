# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 19:47:18 2018

@author: kaysm
"""
import itertools as it

Input=open("Implement PatternToNumber.txt", "r") 
Input=Input.read().split("\n")
Pattern=Input[0]

"""" 
Eigen code: werkt wel maar duurt veelste lang als de pattern bestaat uit meer dan 15 characters
Letters = "ACGT"

count=0
for x in it.product(Letters, repeat=len(Text)):
    if(x==Text):
        print(count)
        break
    else:
        count=count+1
        continue
"""

Mydict =	{"A": 0,"C": 1,"G": 2,"T": 3}

Pattern=Pattern[::-1]
values=[]

for i in range(0,len(Pattern)):
    values.append((4**i)*Mydict[Pattern[i]])

print(sum(values))
    
    





        




         