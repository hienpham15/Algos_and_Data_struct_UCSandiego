#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:30:48 2021

@author: hienpham
"""

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

def read(n):
    #n = int(sys.stdin.readline().strip())
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
      [a, b, c] = map(int, sys.stdin.readline().strip().split())
      key[i] = a
      left[i] = b
      right[i] = c
    return key, left, right


def inOrder(key, left, right):
  inOrder_result = []
  def in_order_traverse(node):
      if left[node] != -1 or right[node] != -1:
          
          if left[node] != -1:
              in_order_traverse(left[node])
              
          inOrder_result.append(key[node])
          
          if right[node] != -1:
              in_order_traverse(right[node])  
      else:
          inOrder_result.append(key[node])
          return 
  in_order_traverse(0)
  return inOrder_result


def IsBinarySearchTree(key, left, right):
  in_order = inOrder(key, left, right)
  
  for i in range(1, len(in_order)):
      if in_order[i-1] >= in_order[i]:
          return False
  return True

"""
n = 7
key = [4, 2, 6, 1, 3 ,5, 7]
left = [1, 3, 5, -1, -1, -1, -1]
right = [2, 4, 6, -1, -1, -1, -1]
IsBinarySearchTree(key, left, right)
"""

def main():
  nodes = int(sys.stdin.readline().strip())
  if nodes == 0:
    print("CORRECT")
    return
  #tree = []
  #for i in range(nodes):
  #  tree.append(list(map(int, sys.stdin.readline().strip().split())))
  key, left, right = read(nodes)
  
  if IsBinarySearchTree(key, left, right):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
