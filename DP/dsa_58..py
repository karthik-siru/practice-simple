'''
Idea : 
 
  Optimal Substructure : 
    
        if the first character is from C matches with the first character of A 

        then we have to check in  Interleaving(A+1, B , C+1 )

        same with B ->  Interleaving(A, B+1, C+1)
  
  Overlapping will also be there.        
       Check the pic attaced for more details .


       Now we will construct a dp table of (n+1)*(m+1)  dimensions 

       ->  n = len(A) and i iterator  , m = len(B) and j iterator 

       -> if the character only matches with A , then we will copy the DP[i-1][j]
       -> same for only B , now we will the copy the left side part DP[i][j-1]
       -> if the character matches with the both, then we will check for both 
          left and top boxes .
       ->  No match we will just make it False.



    DP[i][j]  -> whether the string C=[:i+j-1] is interleaving of A[:i] and B[:j]

'''


class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        
        n, m =  len(A), len(B)
        
        if n+m !=  len(C) :
            return False 
        
        dp =  [[False for i in range(n+1)]for ju in range(m+1)]
        
        # base cases 
        # 1) if both the strings are none and interleaving is none 
        dp[0][0] = True 
        
        # if one of the strings are empty 
        for i in range (1,n+1):
            if A[i-1] !=  C[i-1] :
               dp[0][i] =  False 
            else :
                dp[0][i] =  dp[0][i-1]

        # if one of the strings are empty      
        for j in range (1, m+1) :
           if B[j-1] != C[j-1] :
               dp[j][0] = False 
           else :
               dp[j][0] =  dp[j-1][0]
             
               
        for i in range(1, m+1) :
            for j in range(1, n+1)  :
                
                a =  A[j-1]
                b =  B[i-1]
                c =  C[i+j-1]
                
                #only a 
                if a ==c and b !=  c :
                    dp[i][j]  = dp[i][j-1]
                #only b    
                elif a !=c and b ==c :
                    dp[i][j] = dp[i-1][j]
                #both  a and b   
                elif a ==c and b ==c :
                    dp[i][j] =  dp[i-1][j]  or dp[i][j-1]
                # no match    
                else :
                    dp[i][j] = False 
        
        return dp[m][n]