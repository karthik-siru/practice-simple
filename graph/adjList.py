
class adjNode :
    
    def __init__(self, val) -> None:
        self.data = val
        self.next = None 

class graph :
    
    # we can represent graph as a dict and 
    # add to the lists of the node keys 
    # Ex :  graph = { 'a' : ['b' ,'c'] 
    #                 'b' : ['c' , 'd' ]}
    # below is the linked list approach 

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

    
