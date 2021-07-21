#qUESTION : 
'''
Given a binary matrix mat of size n * m, find out the maximum size square sub-matrix with all 1s.

'''

#iDEA : 
'''
 Let's think of the square matrix ending with (i,j)

 -> Think , what can we derive abt (i,j) from (i-1, j) , (i,j-1) ,(i-1 , j-1 )

 ->  The answer is if the mat(i, j)  is 1 , then we can make a square matrix 
     of size 1 + min(
                        ( i-1 , j ), 
                        ( i , j-1 ),
                        ( i-1 , j-1)
                    )

 -> But How ? ... imagine we want to build a 3x3 matrix ,  

              0 1 1 1              0 1 1 1 
              1 1 1 1  --------->  1 1 2 2 
              0 1 1 1              0 1 2 3 


    * the diagonal confirms that , we can form (n-1)x(n-1) matrix 
    * the top value confirms the right part (n-1)x(n-1)
    * the left part confirms the bottom part (n-1)x(n-1)

    * now we have to confirm the n*n by checking the (i,j)  ;)
'''



class Solution:
    def maxSquare(self, n, m, mat):
        # code here
        
        dp = [[0 for i in range(m)] for j in range(n)]
        
        max_val = 0

        #base cases 
        # if there is only single row or single coloumn , 
        # we can just copy the same values of the matrix .
        for i in range(n) :
            dp[i][0]  = mat[i][0]
            max_val =  max(max_val , dp[i][0])
        for j in range(m) : 
            dp[0][j] = mat[0][j]
            max_val =  max(max_val , dp[0][j] )
            
            
        for i in range(1,n) :
            for j in range(1,m) : 
                if mat[i][j] : 
                    dp[i][j] = 1 +  min(dp[i-1][j-1] , dp[i][j-1] , dp[i-1][j])
                else : 
                    dp[i][j]  = 0
                max_val =  max(max_val , dp[i][j])
                
        return max_val 
            