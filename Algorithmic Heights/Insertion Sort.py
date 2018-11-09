# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 19:04:22 2018

@author: kaysm
"""

def swap(l, a, b):
    """Swap items at positions `a` and `b` in list `l`."""
    l[b], l[a] = l[a], l[b]
    return l

def insert_sort(unsorted_list):
    """Insert sort based on psuedocode on unsorted list."""
    number_of_swaps = 0

    for i in range(1, len(unsorted_list)):
        k = i
        while k > 0 and unsorted_list[k] < unsorted_list[k-1]:
            unsorted_list = swap(unsorted_list, k-1, k)
            number_of_swaps += 1
            k -= 1

    return number_of_swaps

if __name__ == '__main__':
    input = open("Insertion Sort.txt", "r") 
    input=input.read().split("\n")
    input_list = list(map(int, input[1].split()))
    print(insert_sort(input_list))