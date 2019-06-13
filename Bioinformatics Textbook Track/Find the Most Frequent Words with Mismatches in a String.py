# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:43:02 2019

@author: kaysm
"""
Input=open("Find the Most Frequent Words with Mismatches in a String.txt", "r") 
Input=Input.read().split("\n")
sequence=Input[0]
k=int(Input[1].split(" ")[0])
d=int(Input[1].split(" ")[1])

def hamming(pattern, text):
    distance=0
    for i in range(0,len(pattern)):
        if(pattern[i]!=text[i]):
            distance=distance+1
    return distance

"find all kmers in text"
kmers=[]
for i in range(0,len(sequence)-k+1):
        kmers.append(sequence[i:i+k])

"find all neigbors of the kmers"
letters=["A", "C", "G", "T"]
possibles=[]
for kmer in kmers:
    for i in range(0,len(kmer)):
        for letter in letters:
            possible=kmer[0:i] +letter+ kmer[i+1:]
            possibles.append(possible)

"count the number of times each neighbor is possible"
occurences=[]
for possible in possibles:
    count=0
    for kmer in kmers:
        if(hamming(possible, kmer)<d+1):
            count=count+1
    occurences.append(count)

"find the most frequent neighbor"
maximum=max(occurences)
indices = [i for i, x in enumerate(occurences) if x == maximum]

result=list(set([possibles[i] for i in indices]))

print(" ".join(result))

        



