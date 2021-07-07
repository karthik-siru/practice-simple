'''
  Given a list of integers nums, write a function that returns 
  the largest sum of non-adjacent numbers.Numbers can be 0 or negative.


  Algorithm : 

      The idea is simple , at each step , we have two choices , whether to include 
      the number in the highest sum or to leave it . 

      1) If we consider it -->  then the sum would be dp[i-2]+ith element 
      2) Else we just take the dp[i-1]   

      at each step hence , finally we will be having the maximum value ;)

'''

class Solution:
    def solve(self, nums):
        if not nums  :
            return 0
        dp = [0 for i in range(len(nums)+1)]

        dp[1] = max(nums[0] , 0 )

        for i in range(1, len(nums)):
            dp[i+1]  = max (dp[i-1]+nums[i] , dp[i]) 
        
        return dp[-1]