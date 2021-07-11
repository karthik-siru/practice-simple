
''' 

'''


#Function to find the maximum possible amount of money we can win.
def optimalStrategyOfGame(arr, n):
    
    # code here
    
    dp = [[0 for i in range(n)]for j in range(n)]
    
    for i in range(n):
        dp[i][i] = arr[i]
        
    for l in range(2, n+1):
        
        for i in range(0, n) :
            j = i +l -1 
            
            if i >= n or  i+1 >= n  or i +2 >=n or j >= n :
                break 
            
            path1 = arr[i] + min(dp[i+2][j] , dp[i+1][j-1])
            path2 = arr[j] + min(dp[i+1][j-1], dp[i][j-2])
            
            dp[i][j] = max(path1 , path2 )
            
    return dp[0][n-1]