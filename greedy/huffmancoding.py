
'''
Works fine with .. different frqueencies only .
'''

class Node : 
    def __init__(self, data ): 
        self.data  = data 
        self.string = "0"
        self.left  = None 
        self.right = None 
           

from heapq import heappush, heappop 

class Solution:
    def huffmanCodes(self,S,f,N):
        # Code here
        res = []
        def getvalues (node , s ): 
            s += node.string 
            if not node.left and not node.right :
                 res.append(s)
            else :
                 getvalues(node.left, s)
                 getvalues(node.right, s)
         
        pq = []
        for i in range(N) : 
            heappush(pq , (f[i],Node(f[i])))
            
        while len(pq) > 1 : 
            vala , a =  heappop(pq)
            valb , b =  heappop(pq)
            
            n =  vala +  valb 
            temp = Node(n)
            if valb <= vala :
                temp.left =  b
                temp.right = a 
                
            else : 
                temp.left =  a
                temp.right = b 
                
            temp.left.string = "0"
            temp.right.string = "1"
                
                
            heappush(pq, (n, temp ))
            
        ph, root =  heappop(pq)
        
        root.string = ""
        
        s  = ""
        
        getvalues(root, s)
        
        return res 
        