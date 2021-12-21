#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:27:02 2021

@author: hienpham
"""

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def SiftDown(array, n, i):
    
    root = i
    left = i*2 + 1
    right = i*2 + 2
    
    if left < n:
        if array[root][0] > array[left][0]:
            root = left
        elif array[root][0] == array[left][0]:
            if array[root][1] > array[left][1]:
                root = left
        
    if right < n:
        if array[root][0] > array[right][0]:
            root = right
        elif array[root][0] == array[right][0]:
            if array[root][1] > array[right][1]:
                root = right
        
    if root != i :
        array[i], array[root] = array[root], array[i]
        SiftDown(array, n, root)


def build_min_heap(array):
    
    n = len(array)
    
    for i in range((n-1)//2, -1, -1):
        SiftDown(array, n, i)


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    #next_free_time = [0] * n_workers
    
    next_free_time = []
    for i in range(n_workers):
        next_free_time.append([0, i])
    
    for job in jobs:
        #next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        next_worker = next_free_time[0][1]
        start_at = next_free_time[0][0]
        result.append(AssignedJob(next_worker, start_at))
        next_free_time[0][0] += job
        SiftDown(next_free_time, n_workers, 0)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()