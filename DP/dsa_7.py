
'''
Idea : 

   Since the array consists of integers only , to divide the array into , 
   2 equal sum sets , the sum of the array must be even ;)
   
   And each subset will have the sum --> array_sum //2 .

   then the question simply meltdowns to the variation of 0/1Knapsack.

   # similarities b/w 01-knapsack and this problem 

 -> given an array 
 -> we need to make some target , which is  array_sum//2 .
 -> Can we do it or not ;) , is the question 

'''


class Solution:
    def equalPartition(self, N, arr):
        # code here
        
        array_sum =  sum(arr)
        if array_sum %2 ==1 :
            return False 
            
        target =  array_sum//2 
        
        dp = [[False for i in range (target+1)] for j in range (N+1)]
        
        for i in range(N+1):
            for j in range(target + 1):
                if j == 0:
                    dp[i][j] = True  
                elif arr[i-1] >  target :
                    dp[i][j] =  dp[i-1][j]
                else :
                    dp[i][j]   =  dp[i-1][j]  or dp[i-1][j-arr[i-1]]
                    
        return dp[-1][-1]