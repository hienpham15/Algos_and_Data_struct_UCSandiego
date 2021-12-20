#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:22:40 2021

@author: hienpham
"""

import sys
import threading

class Node:
    def __init__(self, val):
        self.key = val
        self.children = []
        
    def add_child(self, child):
        self.children.append(child)

    
def build_tree(parents, n):
    nodes = [Node(i) for i in range(n)]
    
    for i in range(n):
        if parents[i] != -1:
            p = parents[i]
            nodes[p].add_child(nodes[i])
        else:
            root = nodes[i]
    return root


def get_height(i, parents, height):
    
    if (parents[i] == -1):
        return 1
 
    if (height[i] != -1):
        return height[i]
 
    height[i] = get_height(parents[i], parents, height) + 1
 
    return height[i]
            

def compute_height(n, parents):
    max_height = 0
    
    height = [-1]*n
    for i in range(n):
        max_height = max(max_height, get_height(i, parents, height))
        
    return max_height


#parents = [4, -1, 4, 1, 1]
#n = 5
#tree = build_tree(parents, n)
#h = compute_height(n, parents)

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()