#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:25:56 2021

@author: hienpham
"""

def SiftDown(arr, n, i, swaps):
    root = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[root] > arr[left]:
        root = left
        
    if right < n and arr[root] > arr[right]:
        root = right
        
    if root != i:
        arr[i] , arr[root] = arr[root], arr[i]
        swaps.append([i, root])
        SiftDown(arr, n, root, swaps)
    
def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    n = len(data)
    
    for i in range(n//2 - 1, -1, -1):
        SiftDown(data, n, i, swaps)
    
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()