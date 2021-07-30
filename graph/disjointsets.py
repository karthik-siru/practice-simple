
from collections import defaultdict 

class Graph : 

    def __init__(self, v) :
        self.v =  v 
        self.adj =  defaultdict(list)

    def addEdge (self, src, dest , weight ) :
        self.adj[src].append((dest, weight))
        self.adj[dest].append((src, weight))

class DisjointSet :

    parent = {}

    def makeSet(self, N ) :
        for i in range(N) :
            self.parent[i] = i 


    def find (self, src ) :

        if self.parent[src] == src :
            return src 
        return self.find(self.parent[src])


    def union (self, a, b ) :

        x =  self.find(a)
        y =  self.find(b) 

        self.parent[x]  = y 


def Unionfind(graph , N ) :

    ds = DisjointSet()
    ds.makeSet(N)

    for u in range(N+1) :

        for v in graph.adj[u] :
            dest , weight  = v[0] , v[1]

            x =  ds.find(u)
            y = ds.find(dest)

            if x == y :
                return True 
            ds.union(x, y)

    return False 

if __name__ == '__main__' :
    
    v = 10 
    edges = [ (0, 1,2) , (0, 5,4) ]# ....]
    g =  Graph(v)

    for edge in edges :
        src , dest , weight =  edge[0] , edge[1] , edge[2]
        g.addEdge(src , dest , weight )

    if Unionfind(g, v) :
       print("cycle found ;)")
    else :
        print("No cycle found ")



