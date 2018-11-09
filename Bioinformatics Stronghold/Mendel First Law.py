# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:27:02 2018

@author: kaysm
"""

Input=open("Mendel First Law.txt", "r") 
Input=Input.read().split(" ")

K,M,N=int(Input[0]),int(Input[1]),int(Input[2])
totalOrganisms=K+M+N

ChanceKK=K/totalOrganisms * ((K-1)/(totalOrganisms-1))
ChanceMM=M/totalOrganisms * ((M-1)/(totalOrganisms-1))
ChanceNN=N/totalOrganisms * ((N-1)/(totalOrganisms-1))
ChanceKM=K/totalOrganisms * (M/(totalOrganisms-1)) *2
ChanceKN=K/totalOrganisms * (N/(totalOrganisms-1)) *2
ChanceMN=M/totalOrganisms * (N/(totalOrganisms-1)) *2

Kk=1 * ChanceKK
Mm=3/4 * ChanceMM
Nn=0 * ChanceNN
Km=1 * ChanceKM
Kn=1 * ChanceKN
Mn=1/2 * ChanceMN

Totaal= Kk+Mm+Nn+Km+Kn+Mn

print(Totaal)





