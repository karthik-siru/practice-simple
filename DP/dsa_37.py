'''
Idea : We will maintain an array of length n+1 , 
 
dp[i] ->  whether we can break the string s[:i+1] into words from dictionary

So , for each i we check for previous values where the we can break the string 

->  Suppose we found such an index k , then we will then check whether the
    remaining string from the k+1th  index to i is in the dictionary ,
    If exists we can divide the string otherwise no .

'''

def wordBreak(s, dictionary):
    # Complete this function
    n =  len(s)
    dp = [False for i in range(n+1)]
    
    dp[0]  = True 
    i = 1
    while i <  n +1 : 
        for j in range(i):
            if dp[j] and s[j:i]  in dictionary :
                dp[i]  = True 
                
        i +=  1
    return dp[n]