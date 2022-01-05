# python3

import sys

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
        return count
            
#adj = [[1], [], [0], [0]]
#adj = [[], [], [0], []]
#adj = [[], [0], [0, 1], [0, 2], [1, 2]]
#adj = [[1], [2], [0, 3], []]  
#adj = [[1], [2], [3, 4], [0], [5], [6], [4, 7], []]

#kosa = Kosaraju(adj)
#ans = kosa.main()

def number_of_strongly_connected_components(adj):
    #Kosaraju's algorithm: DFS > Reverse Graph > DFS
    
    kosa = Kosaraju(adj)
    result = kosa.main()   
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
