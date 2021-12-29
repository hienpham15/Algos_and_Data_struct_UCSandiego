#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:30:07 2021

@author: hienpham
"""

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.inOrder_result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def in_order_traverse(node):
        if self.left[node] != -1 or self.right[node] != -1:
            if self.left[node] != -1:
                in_order_traverse(self.left[node])
            #inOrder_result.append(path)
            
            self.inOrder_result.append(self.key[node])
            
            if self.right[node] != -1:
                in_order_traverse(self.right[node])

            #inOrder_result.append(path)
        else:
            self.inOrder_result.append(self.key[node])
            return
    
    in_order_traverse(0)
    return self.inOrder_result


  def preOrder(self):
    self.preOrder_result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def pre_order_traverse(node):
        if self.left[node] != -1 or self.right[node] != -1:
            self.preOrder_result.append(self.key[node])
            
            if self.left[node] != -1:
                pre_order_traverse(self.left[node])
            #inOrder_result.append(path)
            
            if self.right[node] != -1:
                pre_order_traverse(self.right[node])

            #inOrder_result.append(path)
        else:
            self.preOrder_result.append(self.key[node])
            return
    
    pre_order_traverse(0)
    return self.preOrder_result


  def postOrder(self):
    self.postOrder_result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    def post_order_traverse(node):
        if self.left[node] != -1 or self.right[node] != -1:
            
            if self.left[node] != -1:
                post_order_traverse(self.left[node])
            #inOrder_result.append(path)
            
            if self.right[node] != -1:
                post_order_traverse(self.right[node])
                
            self.postOrder_result.append(self.key[node])

            #inOrder_result.append(path)
        else:
            self.postOrder_result.append(self.key[node])
            return
    
    post_order_traverse(0)
    return self.postOrder_result


def inOrder(key, left, right):
  inOrder_result = []
  # Finish the implementation
  # You may need to add a new recursive method to do that
  def in_order_traverse(node):
      if left[node] != -1 or right[node] != -1:
          
          if left[node] != -1:
              in_order_traverse(left[node])
          #inOrder_result.append(path)
          
          #inOrder_result.append(key[node])
          
          if right[node] != -1:
              in_order_traverse(right[node])
          
          inOrder_result.append(key[node])
          #inOrder_result.append(path)
      else:
          inOrder_result.append(key[node])
          return 
  
  in_order_traverse(0)
  return inOrder_result

"""
n = 5
key = [4, 2, 5, 1, 3]
left = [1, 3, -1, -1, -1]
right = [2, 4, -1, -1, -1]


n = 10
key = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
left = [7, -1, -1, 8, 3, -1, 1, 5, -1, -1]
right = [2, -1, 6, 9, -1, -1, -1, 4, -1, -1]
res = inOrder(key, left, right)
"""

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()