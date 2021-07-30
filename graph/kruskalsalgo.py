# Kruskal's Algorithm : 

'''
KRUSKAL(graph G)
 
MST = {}
 
for each vertex v belonging G.V:
    MAKE-SET(v)
 
for each (u, v) in G.E ordered by weight(u, v), increasing:
    if adding this doesn't make a cycle , then add to mst 
    if FIND-SET(u) != FIND-SET(v):
        add {(u, v)} to set MST
        UNION(u, v)
 
return MST


IF the graph is not connected , then Kruskal's Algo gives MST forest .

'''


from . import disjointsets 

ds =  disjointsets.DisjointSet()

def kruskalAlgo (edges , N ) :

    ds.makeSet(N)
    edges.sort(key = lambda x : x[2])

    mst = []

    index = 0 

    while index <=  N-1 : 
        src, dest , weight = edges[index]

        x =  ds.find(src)
        y =  ds.find(dest)

        if x != y :
            ds.union(src, dest)
            mst.append((src, dest , weight))

    return mst 
        

