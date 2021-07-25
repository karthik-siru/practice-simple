# qUESTION : 
'''
Check whether a route exits between src and destination in the given graph.
'''

# aPPROACH :
'''

In this approach , we will use bfs to traverse the graph . and we note the 
visited graphs, and whenever we found the dest  node , we can confirm that 
route exits if not we can continue our search . 
if not found, then no route exits .

'''

from collections import defaultdict, deque

class Solution :

    def __init__(self, vertices ):
        self.v  =  vertices 
        self.graph =  defaultdict(list)

    def bfs (self, src , dest ) :

        visited =[False]*(self.v)
        
        if src == dest :
            return True 
        visited[src] = True 
        q =  deque()
        q.append(src) 

        while q :
            u = q.popleft()

            for v in self.graph[u] :
                if not visited[v] :
                    if v == dest :
                        return True 
                    visited[v] = True 
                    q.append(v)
        return False
        
    def checkRoute(self,src, dest):

        if self.bfs(src,dest):
   
            print("Route exits")

        else :
            pas