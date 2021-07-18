'''
 Idea :     
      This is a variation of CoinChange problem , 
    ->  there , we found minimum number of coins to make change 

     Strategy : (for uniqueWaysOptimised )    
     ->  we can choose any number of coins of same value 
         but once we move we cannot choose that coin . 
     ->  the first loop handles ,when we can choose only coin of value 3 .
     ->  second loop for 5 and so on .
'''

class  Solution :

    def uniqueWaysNaive(n, arr):
        # arr ->  coins denominations array 

        dp = [[0 for i in range (len(arr)+1)] for j in range(n+1)]

        #base cases
        # Target_amount ==0  ->  no.of ways = 1 
        # coin denominations ==0  -> no .of ways = 0 

        for i in range(len(arr) + 1):
            for j in range (n+1) :
                if j ==0 : 
                    dp[i][j] = 1
                elif i ==0  : 
                    dp[i][j]  = 0
                elif arr[i] > j :
                    dp[i-1][j]
                else : 
                    dp[i][j] =  dp[i-1][j] + dp[i-1][j-arr[i-1]]
        return dp[len(arr)][n]
    
    def uniqueWaysOptimised(n) :
        
        dp = [0]*(n+1)
        
        #base case 
        dp[0] = 1 

        # when we have only 3 value coins 
        for i in range (3, n+1) :
            dp[i] +=  dp[i-3]
        # when we have 3 qnd 5 value coins 
        for i in range(5, n+1) :
            dp[i] =  dp[i-5]
        # when we have 3,5,10 coins .
        for i in range(10, n+1) :
            dp[i] =  dp[i-10]

        return dp[n]