#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:31:59 2021

@author: hienpham
"""

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
            sub = self.s[i: j+1]
            self.s = self.s[:i] + self.s[j+1:]
            if k == 0:
                self.s = sub + self.s
            else:
                self.s = self.s[:k] + sub + self.s[k:]

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.s)
