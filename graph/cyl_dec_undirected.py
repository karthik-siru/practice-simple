from collections import defaultdict, deque

class graph :
    def __init__(self, vertices) -> None:
        self.graph = defaultdict(list)
        self.v = vertices 
    def addEdge(self, src , dest):
        self.graph[src].append(dest)
        self.graph[dest].appedn(src)
    
    # this function checks for a cycle in the graph 
    # starting with src 
    def DetectCycleBFS(self, src , visited ) :
          
        # mark the src as visited 
        visited[src] = True 
        
        # make a queue 
        q =  deque()
        #append the src and parent as -1 (NONE)
        q.append((src, -1))

        while q:

            ( u , parent )= q.popleft()

            for v in self.graph[u] :
                #  if node not visited 
                # then visit them and push into the stack 
                if not visited[v] :
                    visited[v] = True 
                    q.append(v , u )
                
                # if the node is already visited and 
                # and if it is not the parent (coz parent will also be in the adj[u])
                # then there is a cycle ;) 
                elif v != parent :
                    return True  
        
        return False 

    
    # this function checks for all the non visited nodes 
    # and also covers the disconnected graphhs too .
    def bfsCycleDetect(self) :
        # keep ttrack of visited elements 
        visited = [False]*(self.v)

        for i in range(self.v) :
            if not visited[i]  and self.DetectCycleBFS(i , visited ) :
                return True 
        return False 

#--------------------------------------------------- #

    ## CYCLE DETECTION IN UNDIRECTED GRAPH USING DFS 


    def dfsVisit (self, src , visited, parent ) :
        visited[src]  = True 
        
        for dest in self.graph[src] :
            if not visited[dest] :
                if self.dfsVisit(dest , visited , src) :
                    return True 
            elif dest != parent :
                return True 

        return False 


    def dfs (self) :
       
       visited = [False ]*(self.v)

       for u in range(self.v) :
           if not visited[u] and self.dfsVisit(u , visited , -1 ) :
               return True 
       return False 

