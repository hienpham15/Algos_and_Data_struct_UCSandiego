# python3

import sys


def explore(v):
    visited[v] = 1
    for vertice in adj[v]:
        if visited[vertice] == 0:
            explore(vertice)


def reach(adj, x, y):
    global visited
    explore(x)
    if visited[y] == 1:
        return 1
    else:
        return 0

#n, m = 4, 4
#x, y = 0, 3
#adj = [[], [2], [1, 3], [2]]
#visited = [0]*n
#ans = reach(adj, x, y)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    visited = [0]*n
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
