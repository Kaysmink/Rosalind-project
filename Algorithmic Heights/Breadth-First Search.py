# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:16:54 2019

@author: kaysm
"""
Input=open("Breadth-First Search.txt", "r") 
Input=Input.read().split("\n")

n=int(Input[0].split(" ")[0])

connections=[[] for x in range(n+1)]
results=[-1 for x in range(n+1)]    
Input=Input[1:]
for connection in Input:
    x,y=connection.split(" ")
    x,y=int(x), int(y)
    connections[x].append(y)

known=[1]
results[1]=0

while(known):
    x=known.pop(0)
    for number in connections[x]:
        if(results[number]==-1):
            known.append(number)  
            results[number]=results[x]+1
results=results[1:]

print(" ".join(list(map(str,results))))
    
    



