
'''
Variation of Kadane's Algorithm . 

'''

class Solution:
    
    def KadanesAlgo(self,a):
        
        global_min = 999999
        local_min =0
        
        for i in a : 
            local_min =  max(i , local_min + i )
            
            if local_min <  global_min :
                global_min =  local_min 
                
        return global_min 