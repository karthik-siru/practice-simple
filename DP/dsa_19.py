'''
# This is a variant of 0-1 Knapsack ;)

Idea : 
  This problem can be solved using dynamic programming where 
  dp[i][j] = number of subsequences having product less than j 
             and using first i terms of the array. 
           = Which can be obtained by : number of subsequences using first i-1 terms + 
                                        number of subsequences that can be formed using i-th term. 

'''

class Solution : 
    def subProductLessThanK(self, a, k ) :
        
        dp =  [[0 for i in range(k+1)] for j in range (len(a)+1)]

        for i in range(len(a) +1 ) : 
            for j in range(k+1) : 
                #base case 
                if  i ==0  or j == 0 : 
                    dp[i][j]  = 0

                elif a[i-1] > j : 
                    dp[i][j] = dp[i-1][j]
                else : 
                    dp[i][j] =  dp[i-1][j] + dp[i][j//a[i-1]]

        return dp[-1][-1]

