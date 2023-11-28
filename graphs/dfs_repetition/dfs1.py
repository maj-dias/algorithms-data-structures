from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self,u,v) -> None:
        self.graph[u].append(v)
    
    def dfs_util(self, v, visited) -> None:
        visited.add(v)

        #fazer alguma coisa aqui
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited)

    def dfs(self,v):
        visited = set()
        self.dfs_util(v, visited)

def main() -> None:
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    g.dfs(0)

if __name__ == '__main__':
    main()