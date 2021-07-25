
#Approach : 
'''

The Idea is to traverse the graph using dfs for all the nodes , 
If we found any node not visited , then there is a non-connected component 

'''

from collections import defaultdict , deque 

class Solution :

    def __init__(self, values) -> None:
        self.v = values 
        self.graph =  defaultdict(list)

    def addEdge(self, src , dest ) :
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def dfs(self, visited , src ) :
        visited[src]   = True 

        for v in self.graph[src] :
            if not visited[v] :
               self.dfs(visited , v) 

    def numberofConnectedComponents (self) :

        visited = [False]*(self.v)
        
        count = 0 
        
        # if after dfs , we found a new non visited node 
        # then there a new non connected component 
        for i in range(self.v) :
            if not visited[i] : 
                self.dfs(visited , i)
                count +=  1
                
        return count 