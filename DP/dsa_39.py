#qUESTION :
'''
Given an array of non negative integers , check whether 
there exists a subset with sum equal k 

'''



'''
Idea : 
It is variation of 0/1  Knapsack  ;) 

-> include it or exclude it .

'''

class Solution  :

    def subsetSum(self, a, target):
        n =  len(a)
        dp  =  [[0 for i in range (target+1)]  for i in  range(n +1)]

        for i in range(n+1) :
            for j in range(target +1 ) :

                if j == 0:
                    dp[i][j]  = True 
                elif i == 0 : 
                    dp[i][j]  =  False 
                elif a[i-1]  >  target : 
                    dp[i][j]  =  dp[i-1][j]
                else :
                    dp[i][j]  =  dp[i-1][j] or dp[i-1][j-a[i-1]]

        return dp[n][target]