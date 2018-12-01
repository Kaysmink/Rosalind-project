# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 20:42:20 2018

@author: kaysm
"""

from Bio import SeqIO
from Bio.Seq import Seq

sequences=[]

for seq in SeqIO.parse("Locating Restriction Sites.txt", "fasta"):
    sequences.append(seq.seq._data)

seq=sequences[0]

for i in range(0,len(seq)):
    for j in range(4,13):
        if(i+j>len(seq)):
            break
        motif =seq[i:i+j]        
        motif=Seq(motif)
        if(motif==motif.reverse_complement()):
            print(i+1,j)
        

