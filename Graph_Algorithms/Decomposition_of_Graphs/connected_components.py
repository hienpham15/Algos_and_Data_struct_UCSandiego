# python3

import sys


def explore(v):
    visited[v] = 1
    for vertice in adj[v]:
        if visited[vertice] == 0:
            explore(vertice)


def number_of_components(adj):
    result = 0
    n = len(adj)
    global visited
    visited = [0]*n
    
    for i in range(n):
        if visited[i] == 0:
            explore(i)
            result += 1
    return result


#n, m = 4, 4
#adj = [[], [2], [1, 3], [2]]
#ans = number_of_components(adj)


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
    print(number_of_components(adj))