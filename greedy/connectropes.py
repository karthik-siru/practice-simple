
import heapq as hp
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
    
        # code here
        
        hp.heapify(arr)
        
        res = 0
     
    # While size of priority queue
    # is more than 1
        while(len(arr) > 1):
             
            # Extract shortest two ropes from arr
            first = hp.heappop(arr)
            second = hp.heappop(arr)
             
            #Connect the ropes: update result
            # and insert the new rope to arr
            res += first + second
            hp.heappush(arr, first + second)
             
        return res