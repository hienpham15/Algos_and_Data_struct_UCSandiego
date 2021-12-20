#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:20:31 2021

@author: hienpham
"""

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    bracket_dict = {'(': ')', '[': ']', '{': '}'}
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            
        if next in ")]}":
            if opening_brackets_stack:
                bracket, pos = opening_brackets_stack.pop()
                if bracket_dict[bracket] != next:
                    return i+1
            else:
                return i+1
                
    if not opening_brackets_stack:
        return 'Success'
    else:
        return opening_brackets_stack.pop()[1]
                
    
#text = ')'
#ans = find_mismatch(text)

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

    
if __name__ == "__main__":
    main()