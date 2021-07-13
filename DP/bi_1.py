
'''
Similar to number of ways to reach the end with one or two steps ;) 

we can optimize it futher ,since we only need the previous two values .

'''

class Solution:
    def solve(self, message):
        n =  len(message)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 0 if message[0] == "0" else 1 

        for i in range(2,n+1) :
            if 0< int(message[i-1]) <10 :
                dp[i] +=  dp[i-1]
            if 10<= int(  message[i-2]+ message[i-1] ) <  27 :
                dp[i] +=  dp[i-2]

        return dp[-1]