# python3

import sys
import queue

def bipartite(adj):
    check_list = [-1 for _ in range(len(adj))]
    
    for i in range(len(adj)):
        if check_list[i] == -1:
            Q = []
            Q.append(i)
            check_list[i] = 0
            while Q:
                u = Q.pop(0)
                for v in adj[u]:
                    
                    if check_list[v] == check_list[u]:
                        return 0
                    
                    if check_list[v] == -1:
                        if check_list[u] == 0:
                            check_list[v] = 1
                        else:
                            check_list[v] = 0
                        Q.append(v)
    return 1

#adj = [[1, 2, 3], [0, 2], [0, 1], [0]]
#ans = bipartite(adj)

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
    print(bipartite(adj))