#Question :
'''
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

'''


#Idea : 
'''
 It is similar to weighted  interview scheduling problem ;) 
 
 ->  we will sort the pairs according to the finishing time .
 ->  we will find the pre index for all the values such that , it contains the 
     max index , which we can pair it up with . 

  
 ->  Now in pair perspective , we can have two ways 
      * To include it in the longest chain  ->  add 1 plus dp[p[i]]
      * To exclude   -> problem reduces to  n-1 pairs 


'''

class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        
        pairs = sorted(pairs , key = lambda x : x [1])
        
        n = len(pairs)
        
        p = [0]*(n+1)
        
        for i in range(2,n+1):
            for j in range(i, 0, -1): 
                if pairs[j-1][1] <  pairs[i-1][0]: 
                    p[i] = j 
                    break
        
        dp = [0 for i in range(n+1)]
        
        for i in range (1, n+1) :
            dp[i]  =  max(1+dp[p[i]] , dp[i-1])
            
        return dp[-1]