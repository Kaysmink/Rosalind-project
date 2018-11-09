# -*- coding: utf-8 -*-

#My code is working correctly but doesn't give a solution within the required 5 minutes. 
"""
Created on Sat Aug 11 18:53:43 2018

@author: kaysm


Input=open("TestData.txt", "r") 
Input=Input.read().split("\n")

String=Input[0]
values=Input[1].split(" ")

K=int(values[0])
L=int(values[1])
T=int(values[2])

def patternCount(text,pattern):    
    count=0    
    for i in range(0,len(text)-len(pattern)+1):
        if(pattern==text[i:i+len(pattern)]):
            count=count+1
    return count

Patterns=[]
Num=[]
result=""

for i in range(0,len(String)-L+1):
    text=String[i:i+L]
    print(len(String), i)
    for j in range(0,len(text)-K+1):
        Pattern=text[j:j+K]
        if(patternCount(text,Pattern)>=T):
            if(Pattern not in Patterns):
                Patterns.append(Pattern)            
        
for i in range(0,len(Patterns)):
      result=result + Patterns[i] + " "  
      
print(result)
"""

#Not my Code -->

def CheckClumpLength(indicies, t, L):
	'''Checks that a given set of t k-mers falls within a clump of size L.'''
	for i in  range(len(indicies)-t+1):
		if indicies[t+i-1] - indicies[i] <= L:
			return True
	return False

with open('Find Patterns Forming Clumps in a String.txt') as input_data:
	dna, [k, L, t] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]
 # Find all k-mers, count their appearances, and store thier indicies. 
kmer_dict = dict()
for i in range(len(dna)-k+1):
	if dna[i:i+k] in kmer_dict:
		kmer_dict[dna[i:i+k]][0] += 1
		kmer_dict[dna[i:i+k]][1].append(i)
	else:
		kmer_dict[dna[i:i+k]] = [1, [i]]
 # The candidate k-mers that appear at least t times, along with the indicies where they appear.
kmer_candidates = [ [kmer[0],kmer[1][1]] for kmer in kmer_dict.items() if kmer[1][0] >= t]
 # Check that at least t candidate k-mers fall within a clump of size L.
kmer_clumps = []
for candidate in kmer_candidates:
	if CheckClumpLength(candidate[1], t, L):
		kmer_clumps.append(candidate[0])
 # Print and save the solution.
print(' '.join(kmer_clumps))
   
        

