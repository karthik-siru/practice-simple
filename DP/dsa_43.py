'''
Idea : just a variation of LIS .
'''

class Solution:
	def AlternatingaMaxLength(self, nums):
		# Code here
		n =  len(nums)
		if n ==1 :
		    return 1
		dp = [[1 for i in range(2)] for j in range(n+1)]
		
		INT_MIN =  -9999999
		max_value =  INT_MIN
		dp[0] = 0
		
		for i in range(1,n+1):
		    for j in range(1,i):
		        if nums[j-1] < nums[i-1]:
		            dp[i][1] = max(dp[i][1] ,dp[j][0] +1)
		            max_value = max(max_value , dp[i][1])
		        if nums[j-1] >nums[i-1] :
		            dp[i][0] = max(dp[i][0], dp[j][1] + 1)
		            max_value = max(max_value , dp[i][0])
		            
		return max_value 