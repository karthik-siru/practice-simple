'''

   Idea :  Unbounded Knapsack  -->

   -> We can choose any number  of coins of same type , but once we move on 
      we cannot pick the preevious coins .

   -> for every coin , we have to options , whether to include it or exclude it

                    
    #  Decision TREE : 

                            COIN VALUE 
                                |
        greater than target                 less than the target 
               |                                    |
          same as previ                      include             exclude 
                                                |                  |
                                        count += 1               same as prev
                                        target -= coin value                              

'''

class Solution:
    def count(self, coins, n , m): 
        # code here 
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        
            
        for i in range(n+1):
            for j in range(m+1):
                
                if j == 0 :
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j]= 999999
                    
                elif coins[i-1] > j : # coin value greater than the target 
                    dp[i][j] = dp[i-1][j]
                    
                else : # taking min of including and excluding the  current value 
                    dp[i][j] = min (dp[i-1][j] , 1 + dp[i][j-coins[i-1]] )
                    
        return dp[n][m]



'''
Efficient Approach :

let's first  make a 1D dp array of length amount +1
and initialize dp[0]  with 0  (y?)

dp[i] ->  min number of coins needed to make sum i .

while filling the dp table , ask the following questions  ;) 

-> can i use the coin[0], coins[1] , coins[2].... 
-> if we can use that  
            ** take the min of present value and 1+dp[i-coin_value] 

-> finally you will be having the desired in the last block of the dp table.

'''

class Solution_2 :

    def min_coins_change(self, coins , amount) :
        n = len(coins)

        #base cases :
        if amount == 0 :
            return 0  
        if n == 0:
            return "inf"
        # initialization of amount +1 is optional ;) 
        # any bigger value than amount // min(coins) + 1 is allowed)
        dp = [amount + 1 for i in range (n+1)]

        dp[0] = 0

        for i in range(1,amount+1) :
            for coin in coins :
                if coin <= i :
                    dp[i] = min(dp[i] , 1 +dp[i-coin])

        return dp[-1]