#Uses python3

import sys


def dfs(adj, used, order, x):
    
    used[x] = 1
    
    #if not adj[x]:
    #    order.append(x+1)
    #    used[x] = 1
    #    return
    
    for vertex in adj[x]:
        if used[vertex] == 0:
            dfs(adj, used, order, vertex)
     
    order.append(x+1)
    

def toposort(adj):
    used = [0] * len(adj)
    order = [] 
    
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(adj, used, order, i)
    return list(reversed(order))

#adj = [[1], [], [0], [0]]
#adj = [[], [], [0], []]
#adj = [[], [0], [0, 1], [0, 2], [1, 2]]
#adj = [[1], [2], [0, 3], []]
#ans = toposort(adj) 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x, end=' ')