from collections import defaultdict , deque 

class Graph :
    
    def __init__(self, vertices):
        self.v =  vertices 
        self.adj =  {i:[] for i in range(vertices)}
        
    def addEdge (self, word1 , word2 ):
        n = len(word1)
        m =  len(word2)
        
        i = 0
        
        while i < n and i < m  :
            a  =  word1[i]
            b  =  word2[i]

            if a == b :
                i += 1
                continue 
            
            if a != b :
                k1 = ord(a) - ord('a')
                k2 = ord(b) - ord('a')
                if k2 not in self.adj[k1] :
                    self.adj[k1].append(k2)
                break 
    
            
    def TopologicalSort(self, visited , finished , src , time ):
        
        visited[src]  = True 
        
        time += 1 
        
        for v in self.adj[src] :
            if not visited[v] :
                time = self.TopologicalSort(visited , finished , v , time )
            
        
        finished[time] = src 
        time +=  1 
        
        return time 
        

def findOrder(dict, N, k):
    
    g = Graph(k)
    
    for i in range(N) :
        for j in range(i+1, N) :
            g.addEdge(dict[i] , dict[j])
           
    visited =[False]*(k)
    
    time = 0
    finished = [-1]*(2*k)
    
    for i in range(k) :
        if not visited[i] : 
            time = g.TopologicalSort(visited , finished , i , time )
    
    res = ""      
    for i in reversed(range(2*k)) :
        if finished[i] != -1 :
            res += chr(finished[i] + ord('a'))
            
    return res 

N = 5
K = 4
dict = ["baa","abcd","abca","cab","cad"]
print(findOrder(dict , N , K ))