# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:19:48 2018

@author: kaysm
"""

from Bio.Seq import Seq

Input=open("Find Substrings of a Genome Encoding a Given Amino Acid String.txt", "r") 
Input=Input.read().split("\n")
DnaSeq=Input[0]
proteinSeq=Input[1]

for i in range(0,len(DnaSeq)-len(proteinSeq)*3+1):
    seq=Seq(DnaSeq[i:i+len(proteinSeq)*3])
    if(seq.translate()._data==proteinSeq) or seq.reverse_complement().translate()._data==proteinSeq:
        print(seq._data)
        
    
    