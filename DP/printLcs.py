'''
 Idea :  we must have the dp table for finding the max lcs length 

 ->  In that table : 

 
 Case1 ->  if the characters are same ->  dp[i][j]  =  dp[i-1][j-1]+1 
 Case2 ->  get the max from right and left boxes 


 Now , we will go from bottom-right to top , with two iterators for s1 , s2 

 if s1[i-1]  ==  s2[j-1] : 
       add to the result 
       decrement i 
       decrement j 

 else : 
     choose from which the value is adapted (up or left) 

     approach up and left accordingly .


'''

def printLcs(self, dp , s1 , s2 , n  ,m  ) :
      
    i = n
    j = m
    res = ""
    
    while i >0  and j >0 :
        
        #same character add to the result 
        # now go to the diagonal 
        if s1[i-1] == s2[j-1] :
            res += s1[i-1] 
            j -=1 
            i-= 1 
        # if it is from the left , move left 
        elif dp[i][j-1] >  dp[i-1][j] :
            j -=1 
        # else move up
        else : 
            i-= 1 
    return res[::-1]