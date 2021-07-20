#qUestion : 
'''
Number of derangements for n number of elements 
'''

'''

IDea :  Suppose we have n people and n  corresponding houses .

    -> Suppose for the first house we have n-1 possibilities 

    -> If kth person occupies first house 
            * if 1st person occupies kth house ,then the problem reduced to 
               n-2 people and n-2 houses 
            * else , we will figure out with n-1 people and n-1 houses 


    ->  dp[i]  = (n-1)(dp[i-1] + dp[i-2])

'''

class Solution :

    def numberOfDerangements (self, n):
        
        dp =  [0 for i in range(n+1)]

        #base case 
        # ->  no people no shit 
        dp[0]  = 0  
        # -> only one person no choice 
        dp[1]  = 0
        #Two people one way (exchange)
        dp[1] =  1 

        for i in range(2, n+1) : 
            dp[i]  = (i-1)*(dp[i-1] +  dp[i-2])

        return dp[n]
