from collections import DefaultDict

class graph :
    def __init__(self, vertices ) -> None:
        self.graph = DefaultDict(list)
        self.v = vertices 
    def addEdge(self, src , dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

