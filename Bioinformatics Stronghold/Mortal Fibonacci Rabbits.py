# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 20:26:51 2018

@author: kaysm
"""

Input=open("Mortal Fibonacci Rabbits.txt", "r") 
Input=Input.read().split()

N=int(Input[0])
M=int(Input[1])

def mortal_rabbits(n, m):
    sequence = [1, 1]

    for i in range(n - 2):
        new_num = 0
        if i + 2 < m:
            #Normal fibonacci - No deaths yet
            new_num = sequence[i] + sequence[i + 1]
        else:
            #Different reoccurence relation - Accounting for death
            for j in range(m - 1):
                new_num += sequence[i - j]

        sequence.append(new_num)

    return sequence

Amount=mortal_rabbits(N, M)
print(Amount)
print(Amount[len(Amount)-1])
