# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 19:16:58 2018

@author: kaysm
"""
from Bio import ExPASy
from Bio import SwissProt

Input=open("Introduction to Protein Databases.txt", "r") 
Input=Input.read().split("\n")
Input=Input[0]

handle = ExPASy.get_sprot_raw(Input)
record = SwissProt.read(handle)

for item in record.cross_references:
    print(item)
    if(item[0]=="GO" and item[2][0]=="P"):
        print(item[2][2:])
