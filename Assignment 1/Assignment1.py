#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 11:07:19 2023

@author: MichaelKuby
"""

import numpy as np

def linear_search (A : np.ndarray, v : int) -> int:
    for i in range(len(A)):
        if A[i] == v:
            return i
    return None

def binary_search (A : np.ndarray, start : int, end : int, v : int) -> int:
    # Note that A must be sorted
    m = (start + end) // 2
    if (m < start or m > end):
        return None
    if A[m] == v:
        return m
    elif A[m] > v:
        m = binary_search(A, start, m-1, v)
    else:
        m = binary_search(A, m+1, end, v)
    return m

def main():

    
    randomnums = np.random.randint(1,100, 50) # array of random numbers
    x = 50 # the number to be found
    
    """    
    # Use a linear search algorithm that scans through the sequence, looking for v.

    index = linear_search(randomnums, x)
    
    print(index)    
    """
    
    # Use a binary search algorithm that searches through a sorted sequence, looking for v.
    randomnumsSorted = np.sort(randomnums)
    index = binary_search(randomnumsSorted, 0, len(randomnumsSorted), x)
    
    print (index)
    
if __name__ == '__main__':
    main ()