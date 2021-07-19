'''

Idea : 
    we can step left-bottom or bottom or right-bottom . 

    Now wlet's see fromm the other perspective ;) 

    ->  we can reach a block in three ways 
        * top 
        * top-left
        * top-right 

    SO we will choose the maximum of these three and add the 
    value of the matrix and we are done .

'''

class Solution:
    def maximumPath(self, n, Matrix):
        # code here
        
        # here n+2 is to cover the edge cases 
        dp = [[0 for i in range (n+2)] for j in range(n)]
        
        for i in range (1,n+1):
            dp[0][i] = Matrix[0][i-1]
        #variable which contains the max_sum path    
        maximum = max(dp[0])
        for i in range(1,n):
            for j in range(1,n+1):
                dp[i][j] = max(dp[i-1][j] , dp[i-1][j-1] , dp[i-1][j+1]) + Matrix[i][j-1]
                
                maximum = max(maximum , dp[i][j])
                
        return maximum 