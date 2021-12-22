#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:29:07 2021

@author: hienpham
"""

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class LinkList:
    def __init__(self, string):
        self.string = string
        self.next= None

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.hash_map = dict()
        for i in range(bucket_count):
            self.hash_map[i] = []

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            matches = self.hash_map[query.ind]
            self.write_chain(reversed(matches))
        else:            
            ind = self._hash_func(query.s)
            flag = query.s in self.hash_map[ind]
            if query.type == 'find':
                self.write_search_result(flag)
                
            elif query.type == 'add':
                if not flag:
                    self.hash_map[ind].append(query.s)
            else:
                if flag:
                    self.hash_map[ind].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

"""
n_buckets = 5
n_queries = 12
queries = [['add', 'world'], ['add', 'Hell0'], ['check', 4], ['find', 'Wolrd'],
           ['find', 'world'], ['del', 'world'], ['check', 4], ['del', 'Hell0'],
           ['add', 'luck'], ['add', 'GooD'], ['check', 2], ['del', 'good']]

proc = QueryProcessor(n_buckets)
for i in range(n_queries):
    proc.process_query(Query(queries[i]))
"""


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
