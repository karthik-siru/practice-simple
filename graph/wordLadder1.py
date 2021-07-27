from collections import defaultdict ,deque 

class Graph : 
    
    def __init__(self, vertices) :
        self.graph = defaultdict(list)
        self.v = vertices 
        
    def addEdge(self, src , dest ):
        if dest  not in self.graph[src] :
             self.graph[src].append(dest)
        if src not in self.graph[dest] :
             self.graph[dest].append(src)
        
    def bfs (self ):
        
        print(self.graph)
        
        q = deque()
        visited = [False]*(self.v+1)
        
        visited[0] = True 
        
        null = -1 
        q.append(0)
        q.append(null)
            
        count = 1
        
        while q :
            
            u = q.popleft()
        
            
            if u == -1 :
                q.append(null)
                count += 1
                continue 
                
            if u == self.v :
                return count 
                
            for v in self.graph[u] :
                if not visited[v] :
                    q.append(v)
                    visited[v] = True 
                

class Solution:
    
    def validEdge (self, word1 , word2 ):
        
        if len(word1) != len(word2) :
            return False 
        
        i , j = 0 , 0  
        countdif = 0
        while i < len(word1) and j < len(word2) :
            if word1[i] != word2[j] :
                if countdif ==1 :
                    return False 
                countdif +=1 
            i += 1 
            j += 1  
        return True 
        
    
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        
        if wordList[-1] != endWord :
            return 0 
        
        hash = {}
        hash[beginWord] =  0
        count =1 
        for i in wordList :
            hash[i] = count 
            count +=1 
            
        g = Graph(len(wordList))
        
        wordList.insert(0, beginWord )
        
        for i in range(len(wordList)):
            
            for j in range( i+1 , len(wordList)):
                
                if self.validEdge(wordList[i], wordList[j]):
                    g.addEdge(hash[wordList[i]] , hash[wordList[j]])
                    
                    
        return g.bfs()
                
            
        
a =  Solution()

print(a.validEdge("a" , "b"))
            
            