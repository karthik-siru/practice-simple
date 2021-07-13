'''
idea : 
  
   So , let's think from the other direction .

   -> in how many ways , we can reach the block 

   1)  form left 
   2)  from left_up diagonal
   3)  form left_down diagonal 

   while moving to a block , let's pick the maximum of the above three + gold_loot

   the base case is when we have only one coloumn .

'''


class Solution:
    def maxGold(self, n, m, M):
        # code here
        
        # n+2  is to make code look clean ;) i.e to cover the edge cases 
        dp = [[0 for _ in range (m)] for j in range(n+2)]
        
        #Base case 
        for i in range(1,n+1) :
            dp[i][0] =  M[i-1][0]
            
            
        for j in range (1, m) :
            for i in range(1, n+1) :
                     dp[i][j] =  M[i-1][j] + max(dp[i][j-1] , dp[i-1][j-1], dp[i+1][j-1])
                    
                
        max_val = 0 
        
        for i in range (1,n+1):
            max_val =  max(max_val , dp[i][m-1])
            
        return max_val 