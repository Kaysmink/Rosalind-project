# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:38:35 2019

@author: kaysm
"""
from Bio import Seq

Input=open("Translate an RNA String into an Amino Acid String.txt", "r") 
sequence=Input.read().split("\n")[0]

Dna=Seq.back_transcribe(sequence)
print(Seq.translate(Dna))
