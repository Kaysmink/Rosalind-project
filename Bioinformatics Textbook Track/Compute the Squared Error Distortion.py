# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 12:55:55 2019

@author: kaysm
"""
import math
import numpy as np

Input=open("Compute the Squared Error Distortion.txt", "r") 
Input=Input.read().split("--------")

centerPoints=[]
dataPoints=[]
distance=[]

centers=Input[0].strip()
centers=centers.split("\n",1)
k,m=centers[0].split(" ")
centers=centers[1].split("\n")

data=Input[1].strip().split("\n")

for point in centers:
    centerPoints.append(list(map(float,point.split(" "))))

for point in data:
    dataPoints.append(list(map(float,point.split(" "))))

dataPoints=np.array(dataPoints)
centerPoints=np.array(centerPoints)    

distances=[]

for point in dataPoints:
    minDistance=1000000000000000000000000
    for center in centerPoints:
        diff=point-center     
        distance=np.power(diff,2)
        d=math.sqrt(sum(distance))
        
        if(d<minDistance):
            minDistance=d
    distances.append(math.pow(minDistance,2))
        
distortion=sum(distances)/len(dataPoints) 
print(distortion)  





