# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:44:10 2018

@author: kaysm
"""

from Bio.Seq import Seq

Input=open("Introduction to the Bioinformatics Armory.txt", "r") 
Input=Input.read().split("\n")

String=Input[0]
String=Seq(String)

print(String.count("A"), String.count("C"), String.count("G"), String.count("T") )
