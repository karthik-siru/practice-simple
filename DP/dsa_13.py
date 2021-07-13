'''
Idea: 
  Check the both strings from the last  

  if both are same ->  1 + remove last character from the both 
  else :  
      try by removing last charcter from string1 or 
      try removing last character from string-2 

'''


class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        
        dp = [[0 for i in range (y+1)] for j in range(x+1)]
        
        for i in range(1,x+1) :
            for j in range(1,y+1):
                
                if s1[i-1] == s2[j-1] :
                    dp[i][j]  = 1 + dp[i-1][j-1]
                else :
                    dp[i][j] =  max(dp[i-1][j] , dp[i][j-1] )
                    
        return dp[-1][-1]