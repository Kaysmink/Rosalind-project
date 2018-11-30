# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 15:28:04 2018

@author: kaysm
"""
from Bio import SeqIO

sequences=[]
longestMotif=""

for seq in SeqIO.parse("Finding a Shared Motif.txt", "fasta"):
    sequences.append(seq.seq._data)

smallest=1001

for i in range(0,len(sequences)):
    if(len(sequences[i])<smallest):
        smallest=len(sequences[i])
        index=i

for i in range(len(sequences[index]),0,-1):
    for j in range(0,len(sequences[index])):
        motif=sequences[index][j:i]
        if(motif==""):
            continue
        
        stop=0        
        for x in range(0,len(sequences)):
            if(motif not in sequences[x]):
                stop=1
                break
        if(stop==0):
            if(len(motif)>len(longestMotif)):
                longestMotif=motif        

print(longestMotif)
            


