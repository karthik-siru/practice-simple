
class adjNode :
    
    def __init__(self, val) -> None:
        self.data = val
        self.next = None 

class graph :
    
    def __init__(self, vertices ) -> None:
        self.v = vertices
        self.graph = [None]*(vertices)
    
    #function to add node to undirected graph
    def addEdge(self, src , dest ):
        #adding src dest node to the src adj.list
        node = adjNode(dest) 
        node.next = self.graph[src]
        self.graph[src] = node 

        # adding src node to the dest 
        # since it is undirected 
        node =  adjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node 

    #function to add node to a directed graph
    def addEdgeDirected (self,src,dest ):
        node = adjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node 

    def bfs (self , src ):

        # explores the graph level by level . 
        # collects the info abt the nextLevel
        # and traverse them .
        
        level = {src : 0 }
        parent = {src:None}
        
        frontier = [src]
        i =  1 

        while frontier : 
            # next level nodes 
            nextLevel =[]
            # explore the nodes in present level 
            for v in frontier :
                u = self.graph[v] 
                while u :
                    #  checking if it is already visited or not 
                    if u not in level :
                        level[u] = i
                        parent[u] = v 
                        nextLevel.append(u)
                    u = u.next
            # now explore the next level 
            frontier = nextLevel
