'''

Idea : 
   Since we asked the max dif of number of zeroes  - number of ones , 

   ->  Replace all the 0's  with 1 
   ->  Replace all the 1's with -1 

   ->  Now us the Kadane's Algorithm 

'''


class Solution:
    
    def KadanesAlgo(self,a):
        
        global_max = -999999
        local_max =0
        
        for i in a : 
            local_max =  max(i , local_max + i )
            
            if local_max >  global_max :
                global_max =  local_max 
                
        return global_max 
    
    def maxSubstring(self, S):
		# code here
		
        n = len(S)
        
        dp = [0 for i in range(n)]
        
        for i in range(n):
            if S[i] == '1' : 
                dp[i] = -1
            else : 
                dp[i]  = 1
                
        return self.KadanesAlgo(dp)