# main points to be noticed 
'''
->  if we are gonna push a tuple into the priority-queue , then push like ( priority , value )
->  Graph stores in adj.format  along with it stores the weights ..
->  If all the weights are same , then bfs would aslo do the same 
->  Dijkstra works only for non-negative weights 

'''

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
    
    # used to  get the route after the dijkstra algo
    def getRoute(self, prev , i, route ):
        if i != -1 : 
            self.getRoute(prev , prev[i] , route )
            route.append(i)

    def dijkstra (self, src ) :  

        inf =  9999999 
        
        visited = [False]*(self.v)
        # to keep track of the parents 
        prev = [-1]*(self.v)

        # min distances array , initiaised to inf
        dist =[inf]*(self.v)
        dist[src] = 0

        # priority-queue 
        pq = [] 
        visited[src]  = True 

        # pushing the initial node with value 0
        heappush(pq,(0,src))

        while pq :
            
            prior, u =  heappop(pq)
            
            #explore the adjacent nodes 
            for v, weight in self.graph[u] :
                # Relaxation step 
                if not visited[v] and dist[u] + weight < dist[v] :
                    dist[v] = dist[u] + weight 
                    prev[v] = u
                    heappush(pq , (weight , v))

            visited[u] = True 
        
        #  this is to print the path ;) 
        route = []

        for i in range(self.v) :
            if i != src and dist[i] != inf :
                self.getRoute(prev , i, route )
                print(f"the shortest path from {src} ->{i} is {list(route)}: ")
                route = []


g =  Graph(5)

g.addEdge(0,1,10)
g.addEdge(0,4,3)
g.addEdge(1,2,2)
g.addEdge(1,4,4)
g.addEdge(2,3,9)
g.addEdge(3,2,7)
g.addEdge(4,1,1)
g.addEdge(4,2,8)
g.addEdge(4,3,2)

g.dijkstra(0)




