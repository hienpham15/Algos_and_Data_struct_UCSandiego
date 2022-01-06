# python3

import sys
from heapq import heapify, heappush, heappop

#def relax(u, v, adj, cost):
    

def distance(adj, cost, s, t):
    n_vertex = len(adj)
    
    dist = [float('inf') for _ in range(n_vertex)]
    prev = [0 for _ in range(n_vertex)]
    dist[s] = 0
    
    Q = []
    heappush(Q, (0, s))
        
    while Q:
        _, u = heappop(Q)
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                heappush(Q, (dist[v], v))
    if dist[t] != float('inf'):
        return dist[t]
    else:
        return -1


#adj = [[1, 2], [2, 3, 4], [1, 3, 4], [], [3]]
#cost = [[4, 2], [3, 2, 3], [1, 4, 4], [], [1]]
#s, t = 0, 4
#ans = distance(adj, cost, s, t)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))