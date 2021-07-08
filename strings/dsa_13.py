
'''

Algorithm :  if the string values are same , then no edit required here , hence same

as it's  diagonal value , otherwise  ->  1 + min ( diagonal or top  or left )

'''


class Solution:
	def editDistance(self, s, t):
		# Code here
		n = len(s)
		m = len(t)
		dp = [[0 for i in range(n+1)] for j in range(m+1)]
		
		for i in range(n+1):
		    dp[0][i]  = i 
		for j in range(m+1) :
		    dp[j][0] = j 
		    
		for i in range(1, m+1) :
		    for j in range(1, n+1) :
		        if t[i-1] == s[j-1]:
		            dp[i][j]  =  dp[i-1][j-1]
		        else :
		            dp[i][j]  = 1+ min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1])
		return dp[m][n]