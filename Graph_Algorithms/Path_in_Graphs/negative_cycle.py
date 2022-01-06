# python3

import sys


def negative_cycle(adj, cost):
    n_vertex = len(adj)
    dist = [float('inf') for _ in range(n_vertex)]
    prev = [None for _ in range(n_vertex)]
    
    
    for k in range(n_vertex - 1):
        dist[k] = 0
        for u in range(n_vertex):
            for i, v in enumerate(adj[u]):
                if dist[u] != float('inf') and dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    prev[v] = u
    
    for u in range(n_vertex):
        for i, v in enumerate(adj[u]):
            if dist[u] != float('inf') and dist[v] > dist[u] + cost[u][i]:
               return  1
    return 0

#adj = [[1], [2], [0], [0]]
#cost = [[-5], [2], [1], [2]]
#ans = negative_cycle(adj, cost)


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
    print(negative_cycle(adj, cost))