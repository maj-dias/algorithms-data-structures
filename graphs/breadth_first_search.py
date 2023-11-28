from collections import defaultdict;

class graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self,s):
        visited = [False] * (max(self.graph) + 1)

        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0) #first in first out, remove the first position
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i]=True

def main() -> None:
    g = graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.BFS(2)

if __name__ == '__main__':
    main()