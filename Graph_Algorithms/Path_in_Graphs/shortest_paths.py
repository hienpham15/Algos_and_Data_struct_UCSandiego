# python3

import sys
import queue

sys.setrecursionlimit(200000)

class Kosaraju:
    def __init__(self, adj_matrix):
        self.adj = adj_matrix
        self.n_vertex = len(adj_matrix)
        
    def dfs_stack(self, visited, stack, x):
        visited[x] = True
    
        for vertex in self.adj[x]:
            if not visited[vertex]:
                self.dfs_stack(visited, stack, vertex)
        stack.append(x)
    
    
    def transpose_graph(self):
    
        adj_transpose = [[] for _ in range(self.n_vertex)]
        
        for i in range(self.n_vertex):
            if self.adj[i]:
                for v in self.adj[i]:
                    adj_transpose[v].append(i)
        return adj_transpose
    
    
    def dfs_popstack(self, adj_T, visited, x, scc):
        visited[x] = True
        
        for vertex in adj_T[x]:
            if not visited[vertex]:
                self.dfs_popstack(adj_T, visited, vertex, scc)
        
        scc.append(x)
      
      
    def main(self):
        visited = [False for _ in range(self.n_vertex)]
        stack = []
        strongly_connected_component = []
        
        for i in range(self.n_vertex):
            if not visited[i] :
                self.dfs_stack(visited, stack, i)
            
        visited = [False for _ in range(self.n_vertex)]
        graph_T = self.transpose_graph()
        
        while stack:
            scc = []
            x = stack.pop()
            if not visited[x]:
                self.dfs_popstack(graph_T, visited, x, scc)
                strongly_connected_component.append(scc)
        count = len(strongly_connected_component)
        return count, strongly_connected_component
    

def negative_cycle(adj, cost, strongly_connected_component):
    n_vertex = len(adj)
    dist = [float('inf') for _ in range(n_vertex)]
    prev = [None for _ in range(n_vertex)]
    
    neg_v = []
    
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
               for scc in strongly_connected_component:
                   if u in scc:
                       neg_v += scc
    return neg_v


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    prev = [None]*len(adj)
    negative_cycle = queue.Queue()

    reachable[s] = 1
    distance[s] = 0
    for ind in range(len(adj)):
        nothingChanged = True
        for u in range(len(adj)):
            for v in adj[u]:
                v_index = adj[u].index(v)
                if distance[u]!= 10**19 and distance[v] > distance[u] + cost[u][v_index]:
                    nothingChanged = False
                    distance[v] = distance[u] + cost[u][v_index]
                    prev[v] = u
                    reachable[v]=1
                    if ind == len(adj) - 1:
                        negative_cycle.put(v)
                        shortest[v]=0
        if nothingChanged:
            break

    #mark reachable
    for ind in range(len(adj)):
        if distance[ind] < 10**19:
            reachable[ind] = 1

    visited = [False] * len(adj)
    while not negative_cycle.empty():
        u=negative_cycle.get()
        visited[u]=True
        shortest[u] = 0
        for v in adj[u]:
            if visited[v] == False:
                negative_cycle.put(v)
                visited[v]=True
                shortest[v]=0

    distance[s] = 0


#adj = [[1, 2], [2], [4], [2], [3], [0]]
#cost = [[10, 100], [5], [7], [-18], [10], [-1]]
#n = len(adj)
#distance = [10**19] * n
#reachable = [0] * n
#shortest = [1] * n
#s = 0
#shortet_paths(adj, cost, s, distance, reachable, shortest)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])