import heapq
from heapq import heappush , heappop

class Node : 
    def __init___(self, val) : 
        self.data = val
        self.next =None 
        self.bottom =  None 
    # this is useful during comparing two nodes     
    def __lt__(self, other):
        return (self.data <  other.data )

class Solution :   
    def flatten(self,root):
        #Your code here
        
        if not root : 
            return root 
        
        temp  = root
        
        pq = []
        #push all the elements into heap
        while temp : 
            heappush(pq , temp)
            temp =  temp.next 
        
        heapq.heapify(pq)    
        # get the newhead 
        newhead = heappop(pq)
        # assign a temp variable 
        temp = newhead
        
        if newhead.bottom :
            heappush(pq,newhead.bottom )
            
        while pq : 
            
            min = heappop(pq)
            # extract and add the min node 
            temp.bottom =  min 
            temp = temp.bottom 
            # add the bottom node of min
            if min.bottom : 
                heappush(pq, min.bottom)
                
        return newhead 