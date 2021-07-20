#qUESTION : 

'''
Given an array of integers arr[] and a number K.You can pair two numbers of the array if the difference between them is strictly less than K. The task is to find the maximum possible sum of such disjoint pairs. The Sum of P pairs is the sum of all 2P numbers of pairs.

 

Example 1:

Input  : 
arr[] = {3, 5, 10, 15, 17, 12, 9}
K = 4
Output : 
62
Explanation :
Then disjoint pairs with difference less
than K are, (3, 5), (10, 12), (15, 17)
max sum which we can get is 
3 + 5 + 10 + 12 + 15 + 17 = 62
Note that an alternate way to form 
disjoint pairs is,(3, 5), (9, 12), (15, 17)
but this pairing produces less sum.


'''


'''
Idea :  
      our goal is to make the sum maximum ,  so for that we will pair with a[n-1] and a[n-2] , 
      I mean adjacent elements , 
      ->  Suppose we pair them * then our problem reduced to a[:n-2] and ofc we add the sum
          * dp[i]  =  dp[i-2] + a[i] + a[i-1]
      ->  If no pair , we will leave the last element and look at the remaining array 
          * dp[i]  = dp[i-1]
      suppose we sort the array 

'''

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, n, k): 
        # Your code goes here 
        arr.sort()
        dp =  [0 for i in range(n)]
        
        #base cases 
        #one element ->  0 
        
        for i in range(1, n) :
            if arr[i] - arr[i-1] < k : 
                dp[i]  =  arr[i] + arr[i-1] + dp[i-2]
                
            else : 
                dp[i]  = dp[i-1]
                
        return dp[n-1]