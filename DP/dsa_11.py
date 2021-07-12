'''
idea :  See the pic attached with this question for more better understanding . 


'''

class Solution:
    def countWays(self,n,k):
        #code here.
        if n <2 :
            return n*k 
        elif n ==2 :
            return k*k 
        previous_one  = k 
        previous_two = k*k
        modulo = 1000000007 
        res = 0
        for i in range(3, n) :
            res  =  (k-1)*(previous_one +  previous_two)
            previous_one = previous_two 
            previous_two =  res %modulo
        
        return res%modulo