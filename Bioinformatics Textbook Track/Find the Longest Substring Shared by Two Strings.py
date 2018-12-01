# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:25:53 2018

@author: kaysm
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:28:04 2018

@author: kaysm
"""

Input=open("Find the Longest Substring Shared by Two Strings.txt", "r") 
Input=Input.read().split("\n")
seq1=Input[0]
seq2=Input[1]

longestMotif=""

for i in range(len(seq1),0,-1):
    for j in range(0,len(seq1)):
        motif=seq1[j:i]
        if(motif in seq2):
            if(len(motif)>len(longestMotif)):
                longestMotif=motif        

print(longestMotif)
            


