# python3

import sys


def check_cycle(v):
    visited[v] = 1
    ordered[v] = True
    
    for vertex in adj[v]:
        if visited[vertex] == 0:
            if check_cycle(vertex):
                return True
        elif ordered[vertex]:
            return True
        
    ordered[v] = False


def acyclic(adj):
    n = len(adj)
    
    global cycle
    global ordered, visited
    
    cycle = [0]
    visited = [0]*n
    ordered = [False]*n
    
    
    for i in range(n):
        if visited[i] == 0:
            if check_cycle(i):
                return 1
    
    return 0


#n, m = 5, 4
#adj = [[1, 2, 3], [2, 4], [3, 4], [], []]
#ans = acyclic(adj)    


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))