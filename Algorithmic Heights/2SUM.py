# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 19:06:09 2018

@author: kaysm
"""
from collections import defaultdict


def two_sum(a, x):
    '''Returns indices i and j such that a[i] + a[j] = x if they exist, otherwise -1.'''
    # Hash the array, storing the indices corresponding to each element.
    elmt_hash = defaultdict(set)
    for index, e in enumerate(a):
        elmt_hash[e].add(index)

    # Loop over all elements in the hash, checking for the necessary element to complete 2sum.
    for e in elmt_hash:
        if x-e in elmt_hash:
            if x-e == e and len(elmt_hash[e]) > 1:
                # Rosalind indices start at 1.
                return sorted([elmt_hash[e].pop()+1, elmt_hash[e].pop()+1])
            elif x-e != e:
                # Rosalind indices start at 1.
                return sorted([elmt_hash[e].pop()+1, elmt_hash[x-e].pop()+1])

    # If the loop ends 2sum is not possible.
    return -1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('2SUM.txt') as input_data:
        k, n = map(int, input_data.readline().strip().split())
        arrays = [map(int, line.strip().split()) for line in input_data.readlines()]

    # Run the 2sum algorithm on each array, then format the results.
    indices_2sum = [two_sum(a, 0) for a in arrays]
    indices_2sum = [str(x) if type(x) is int else ' '.join(map(str, x)) for x in indices_2sum]

    # Print and save the answer.
    print('\n'.join(indices_2sum))
    
if __name__ == '__main__':
    main()
    
"""
Input=open("TestData.txt", "r") 
Input=Input.read().split("\n")

K=int(Input[0].split(" ")[0])
N=int(Input[0].split(" ")[1])

for i in range(0,K+1):
    Input[i]=Input[i].split(" ")
    Input[i]=list(map(int,  Input[i]))

ListOfArrays=Input[1:K+1]
Results=[]

for i in range(0,len(ListOfArrays)):
    indexes=False
    result=[]
    Max=-1
    for j in range(0,len(ListOfArrays[i])):
        for x in range(0,len(ListOfArrays[i])):
            if(j!=x):
                if(ListOfArrays[i][j]==-ListOfArrays[i][x] |(ListOfArrays[i][j]==0 & ListOfArrays[i][x]==0)):
                    #print(ListOfArrays[i][j],ListOfArrays[i][x])
                    indexes=True
                    if([x+1,j+1] in result):
                        break
                    else:
                        result.append([j+1,x+1])  
                
    for a in range(0,len(result)):
        if(result[a][1]>Max):
            Max=a
            
    if(Max>=0):
        outputString=str(result[Max][0])+" "+ str(result[Max][1])
        print(outputString,i)
    if(indexes==False):
        print(-1,i)
        
"""
                
        



