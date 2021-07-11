class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n =  len(s)
        dp = [[0 for i in range(n)] for j in range(n) ]
        
        for i in range(n) :  # this loop is for single length palindromes 
            dp[i][i]  =  1 
        
        for l in range(2, n+1) : # l is the parameter for the length 
            for i in range(n-l+1) : # i is for the starting index  and 
                                    # j is for the ending index                   
                j = i + l -1 
                if s[i]== s[j] and l ==2 :
                    dp[i][j] = 2
                    
                if s[i] == s[j] :
                    dp[i][j]  =  2 + dp[i+1][j-1]
                else :
                    dp[i][j]  =  max(dp[i+1][j] , dp[i][j-1])
                        
        return dp[0][n-1]
                