'''
-> Given , a DAG means no backedge will exits .
-> for backedge for any edge(u,v)->  finishtime[u] <= finishtime[v]
-> We will sort the elements according to their finishing times 

'''

from collections import defaultdict

class Solution :

    def __init__(self , vertices ) -> None:
        self.v =  vertices 
        self.adj = defaultdict(list)

    def addEdge (self, src , dest , weight ) :
        self.adj[src].append((dest, weight))

    def dfs (self,src ,visited , finished , time ):

        visited [src]  = True 

        time +=  1 

        for edge  in self.adj[src] :
            v =  edge[0]
            weight =  edge[1]
            
            # IF the node is not visited 
            if not visited[v] :
                self.dfs(v, visited , finished , time )

        time += 1
        
        finished[time] = src 

    def topologicalSort(self) :
        '''
         Here , we are storing the vertices according to the time ;) 
         If you thought to store according to the vertex , 
         then you have to sort the list to get the topological order.
        '''

        visited = [False]*(self.v)
        finished = [-1](self.v)
        
        time = 0
        for i in range(self.v) :
            if not visited[i] :
                self.dfs(i, visited , finished , time )
        
        # print the order according to finished time : 
        for i in reversed(self.v) :
            if finished[i] != -1 :
                print(f"->{finished[i]}", end = "")


