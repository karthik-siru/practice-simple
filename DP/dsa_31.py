'''
-> Always look for these two properties  

   1) Optimal substructure 
   2) Overlapping 

   The longest common suffix has following optimal substructure property. 
   If last characters match, then we reduce both lengths by 1 
   LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1] 
   If last characters do not match, then result is 0, i.e., 
   LCSuff(X, Y, m, n) = 0 if (X[m-1] != Y[n-1])
   Now we consider suffixes of different substrings ending at different indexes. 
   The maximum length Longest Common Suffix is the longest common substring. 
   LCSubStr(X, Y, m, n) = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m and 1 <= j <= n 

'''

class Solution:
    
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        LcSuffix = [[0 for i in range(n+1)] for j in range (m+1)]
        
        result = 0
        
        for i in range (m+1):
            for j in range(n+1) :
                if i ==0 or j ==0 :
                    LcSuffix[i][j]  = 0
                elif S2[i-1] == S1[j-1] : 
                    LcSuffix[i][j] = 1 + LcSuffix[i-1][j-1]
                    result = max(result , LcSuffix[i][j])
                else : 
                    LcSuffix[i][j] = 0
                    
        return result 