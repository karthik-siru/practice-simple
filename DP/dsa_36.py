
'''
The only diff b/w 0-1Knapsack and this is that while selecting 

max ( dp[i-1][j] , val[i-1]+dp[i][j-wt[i-1]] ) , we don't  decrease i by 1 , 
because we can still use it . 

Whereas , in 0-1 KnapSack , we  can either take or leave ,so we decrement i by 1.

'''

class Solution:
    def knapSack(self, N, W, val, wt):
        # code here
        
        dp =  [[0 for i in range(W+1)]  for j in range (N+1)]
        
        for i in range (N+1):
            for j in range (W+1):
                if i ==0  or j ==0 :
                    dp[i][j] = 0
                elif wt[i-1] >  j: 
                    dp[i][j]  = dp[i-1][j]
                else : 
                    dp[i][j]  =  max ( dp[i-1][j] , val[i-1]+dp[i][j-wt[i-1]] )
                    
        return dp[-1][-1]