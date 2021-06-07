
'''

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

'''

'''

The idea is pretty interesting .. note that for every even number the lsb = 0 and for odd lsb = 1

right shift the given number ( optimal substructure  )

hence , if n is even ---->  dp[n] =  dp[n//2]
        if n is odd  ---->  dp[n] = 1 + dp[n//2]

'''


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        
        if n < 1 :
            return [0]
        
        dp[1] = 1
        
        for i in range (2, n+1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else :
                dp[i] = 1 + dp[i//2]
                
        return dp
