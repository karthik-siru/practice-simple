'''
Idea :  if the weight > limit  --> leave it . 

    if fits in the bag , then try max of including and excluding the value .

'''


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, N):
       
        # code here
        
        dp = [[0 for i in range(W+1)] for j in range (N+1)]
        
        for i in range(N+1) :
            for j in range(W+1) :
                if i ==0 or j == 0:
                    dp[i][j] = 0 
                elif wt[i-1] > j :
                    dp[i][j] = dp[i-1][j]
                else :
                    dp[i][j] =  max (dp[i-1][j] , val[i-1] +dp[i-1][j-wt[i-1]] )
                    
        return dp[N][W]