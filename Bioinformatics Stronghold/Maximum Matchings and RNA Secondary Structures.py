# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:13:16 2018

@author: kaysm
"""
from Bio import SeqIO
from Bio.Seq import Seq
import math

sequences=[]

for seq in SeqIO.parse("Maximum Matchings and RNA Secondary Structures.txt", "fasta"):
    sequences.append(seq.seq._data)
    
seq=Seq(sequences[0])

A,C,U,G = seq.count("A"),seq.count("C"),seq.count("U"),seq.count("G")

answer=math.factorial(max(A,U))//math.factorial(abs(A-U)) * math.factorial(max(C,G))//math.factorial(abs(C-G))
print(answer)

