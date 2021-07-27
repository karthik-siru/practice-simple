from collections import defaultdict 
from heapq import heappop ,heappush

class Graph : 
    
    # number of vertice needed durinng initialisation 
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.v = vertices 
    
    # Adding the edge 
    def addEdge(self, src, dest , weight ) :
        self.graph[src].append((dest, weight))

    def bellmanFord(self, src ) :
        
        inf =  99999999
        dist = [inf]*(self.v)

        dist[src] = 0 

        # why ? we have to repeat the relaxation  of all the edges for v-1 times
        # Since the longest path without cycle is v-1
        for i in range(self.v -1 ) : 
            # checking for all the edges 
            for vertex in range(self.v) :
                #Relaxation step 
                for edge in self.graph[vertex] : 
                    u =  vertex 
                    v =  edge[0]
                    weight =  edge[1]

                    if dist[u] + weight < dist[v] :
                        dist[v] = dist[u] + weight 
        
        # after all the above steps all the nodes are at their min dist from src
        # we again , check all the edges once again
        for vertex in range(self.v) :

                for edge in self.graph[vertex] : 
                    u =  vertex 
                    v =  edge[0]
                    weight =  edge[1]
                    
                    # any shorter path found, indicates the presence of -ve cycle 
                    if dist[u] + weight < dist[v] :
                        return True 

        # if not no -ve cycle ;) 
        return False 


        

