'''
 Same as finding the minimum coins , except we add the values of including and 
 excluding .

 This is using 2D array 

 For better solution scroll down ;)

'''

class Solution:
    def count(self, coins, n , m): 
        # code here 
        
        if n == 0:
            if m == 0:
                return 1 
            else :
                return 0 
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
            
        for i in range(1, n+1):
            for j in range(m+1):
                
                if j == 0 :
                    dp[i][j] = 1
                    
                elif coins[i-1] > j :
                    dp[i][j] = dp[i-1][j]
                    
                else :
                    dp[i][j] = dp[i-1][j] + + dp[i][j-coins[i-1]] 
                    
        return dp[n][m]




'''
Another - APPROACH : 

Same logic as above , but  a good algoithm .

'''

class Solution_2 :
    
    def count(coins , amount ):
 
        dp = [0] * (amount + 1)
        dp[0] = 1
    
        for i in range(len(coins)):
            j =coins[i]
            while j <= amount:
                dp[j] += dp[j -coins[i]]
                j = j + 1
    
        return dp[amount]