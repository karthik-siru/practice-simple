'''
Idea:  Suppose , we are dealing with the string[i:j+1]  . SO now 

     ->  if s[i] equals to s[j] 
          
          * add count of palindromic subsequences  s[i+1 : j+1]
          * add count of palindromic subsequences  s[i:j]

          * Now s[i] and s[j]  together make a palindrome . add +  q

     ->  If s[i]  not equals s[j]

          * add count of palindromic subsequences  s[i+1 : j+1]
          * add count of palindromic subsequences  s[i:j]

          * now we counted s[i-1][j-1]  two times , hence subtract once .


     ->  **Note*** that , we didn't subtracted the dp[i-1][j-1] from the first case
         b'coz 

         * for the first count themself itself , but for the second count 
         * we can make palindromes , like this s[i]......s[j] .

'''

class Solution : 

    def  CountPalindromicSubs(self, s) :
        
        n =  len(s)
        dp = [ [0 for i in range(n+2)] for j in range(n+2) ]

        #base case 
        # if the string length is  1 
        for i in range (n) : 
            dp[i][i]  =  1 

        for l in range (2, n+1): #l is the variable length 
            for i in range(n): # i is the startignindex of it 

                j = l+i -1  # j is the end index of the variable string

                if s[i]  == s[j] : 
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] + 1
                else : 
                    dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i-1][j-1]

        return dp[0][n-1]
