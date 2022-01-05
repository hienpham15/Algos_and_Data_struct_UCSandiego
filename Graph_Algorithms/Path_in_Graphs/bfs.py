# python3

import sys
import queue
import math

def distance(adj, s, t):
    n_vertex = len(adj)
    dist = [math.inf for _ in range(n_vertex)]
    prev = [None for _ in range(n_vertex)]
    
    dist[s] = 0
    Q = []
    Q.append(s)
    while Q:
        u = Q.pop(0)
        for v in adj[u]:
            if dist[v] == math.inf:
                Q.append(v)
                dist[v] = dist[u] + 1
                prev[v] = u
        
    if dist[t] != math.inf:
        return dist[t]
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
