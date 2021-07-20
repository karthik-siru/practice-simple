'''
Idea : 

 Same as Longest Increasing Subsequence ;) , just a little bit variation.

'''

class Solution:
    def longestSubsequence(self, n, a):
        # code here
        
        dp =  [1 for i in range(n)]
        
        for i in range(1,n) :
           for j in range(i) : 
               if a[j] == a[i] +1 or a[j] == a[i]-1 :
                   dp[i]  = max(dp[i]  , 1+  dp[j])
                   
        return max(dp)