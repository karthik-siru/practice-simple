from collections import DefaultDict

# Cycle detection in directed  graph .


class graph :
    def __init__(self , vertices ) -> None:
        self.graph = DefaultDict(list)
        self.v = vertices 
    def addEdge(self, src , dest):
        self.graph[src].append(dest)
    
    def recDfsCycleDetection (self, visited , recStack , vertex ):
        
        # mark the node 
        # add it to the recursive stack 
        visited[vertex] = True 
        recStack[vertex]  = True 
        
        # explore all the neighbours of the node 
        # if it is already in the stack , we found our cycle 
        # else explore all the non visited nodes 
        for neighbour in self.graph[vertex] :
            if not visited[neighbour]  :
                if self.recDfsCycleDetection(visited , recStack , neighbour) == True :
                    return True 
            elif recStack[neighbour] == True :
                return True 
        # we are removing this beccause 
        # now we moved back of this node and 
        # is no longer present in the stack .
        recStack[vertex] = False 

        return False  

    def dfsCycleCheck(self ):
        visited = [False]*(self.v+1) 
        recStack = [False]*(self.v+1)

        # all the nodes are numbers 
        # we traverse all of them one by one .

        for node in range(self.v):
                if not visited[node] :
                    if self.recDfsCycleDetection(visited , recStack , node) == True :
                        return True 
        return False 