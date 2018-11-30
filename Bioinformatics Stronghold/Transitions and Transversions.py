# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 16:34:31 2018

@author: kaysm
"""

from Bio import SeqIO

dic={"A":"G", "G":"A", "C":"T", "T":"C"}

sequences=[]

for seq in SeqIO.parse("rosalind_tran.txt", "fasta"):
    sequences.append(seq.seq._data)   
    
transition=0
transversion=0

for i in range(0,len(sequences[0])):
    if(sequences[0][i]==sequences[1][i]):
        continue
    elif(dic[sequences[0][i]]==sequences[1][i]):
        transition=transition+1
    else:
        transversion=transversion+1
        
print(transition/transversion)
    