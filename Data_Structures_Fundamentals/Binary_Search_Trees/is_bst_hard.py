#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:31:09 2021

@author: hienpham
"""

import sys, threading
import math

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**30)  # new thread will get stack of such size

prev = -math.inf

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
  node_flag = []
  def in_order_traverse(node):
      if left[node] != -1 or right[node] != -1:
          
          if left[node] != -1:
              in_order_traverse(left[node])
              
          inOrder_result.append(key[node])
          node_flag.append(1)
          
          if right[node] != -1:
              in_order_traverse(right[node])  
      else:
          inOrder_result.append(key[node])
          node_flag.append(0)
          return 
  in_order_traverse(0)
  return inOrder_result, node_flag


def IsBinarySearchTree(key, left, right):
  in_order, node_flag = inOrder(key, left, right)
  
  for i in range(1, len(in_order)):
      if in_order[i-1] > in_order[i]:
          return False
      elif in_order[i-1] == in_order[i]:
          if node_flag[i-1] != 1:
              return False
  return True

"""
n = 3
key = [2, 1, 2]
left = [1, -1, -1]
right = [2, -1, -1]
ans = IsBinarySearchTree(key, left, right)
"""

def main():
  nodes = int(sys.stdin.readline().strip())
  if nodes == 0:
      print("CORRECT")
  #tree = []
  #for i in range(nodes):
  #for i in range(nodes):
  #  tree.append(list(map(int, sys.stdin.readline().strip().split())))
  key, left, right = read(nodes)
  if IsBinarySearchTree(key, left, right):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
