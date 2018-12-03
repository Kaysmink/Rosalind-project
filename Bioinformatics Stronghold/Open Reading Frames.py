# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:59:41 2018

@author: kaysm
"""

from Bio import SeqIO
from Bio.Seq import Seq

sequences=[]

for seq in SeqIO.parse("Open Reading Frames.txt", "fasta"):
    sequences.append(seq.seq._data)

seq=sequences[0]

def open_reading_frames(seq):
    stopCodons=["TAG","TGA","TAA"]
    for i in range(1,len(seq)-1):
        codon=seq[i-1:i+2]
        if(codon=="ATG"):
            frame=codon
            j=i+3
            while(seq[j-1:j+2] not in stopCodons):
                    frame=frame+seq[j-1:j+2]
                    #print(frame)
                    j=j+3
                    if(j>len(seq)):
                        if(seq[len(frame):-3]) not in stopCodons:
                            frame=""                              
                        break
            frame=Seq(frame) 
            if(frame.translate()._data not in answer and frame.translate()._data !=""):
                answer.append(frame.translate()._data)
    return answer
      
answer=open_reading_frames(seq)
reverse_complement_seq=Seq(seq).reverse_complement()._data
open_reading_frames(reverse_complement_seq)

print("\n".join(answer))







