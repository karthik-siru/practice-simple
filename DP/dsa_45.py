'''

Winning will be decided by the person who picks second 

Idea :  When will A can win ?  
        ->  when he can grab the all remaining coins at this step.

       ->  dp[i]  =  whether A can win or not with value i 

       if he didn't won dp[i-1] , then he can pick 1 now and can win 
       same applies for x and y .
'''

class Solution :

    def predictWinner (self, n,x,y):

        dp = [0  for i in range(n+1)]
        dp[0] = False 
        dp[1] = True
        for i in range (2, n+1):

            if i >=1  and not dp[i-1]:
                dp[i]  = True 
            elif i>=x and not dp[i-x] :
                dp[i]  =  True 
            elif i>= y and not dp[i-y] : 
                dp[i]  = True 
            else : 
                dp[i]  = False 

        return dp[n]

