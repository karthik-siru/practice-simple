#qUESTION : 
'''
   Given a 2D matrix, Find the maximum rectangular matrix with sum 0.
'''


'''
Idea :  
        -> fix the left limit and the right limit for the matrix .
        -> Now calculate the row-wise sum for all the rows from left to right 
        -> store the row-wise sums in an array temp,
        ->  Now apply the "Kadane's Algorithm " for the temp 
        ->  Keep track of the max_value so far ;)
        * Amazing isn't it ;) 

Same as maximum sub matrix sum , except change the Kadanes algo to the algo , which 
can give the longest continous subarray with sum 0  .

'''


class Solution: 
    
    def SubArraySum0(self,arr):
        s = set() 
        # store the sums in the set , if the sum is already seen ,we found the subarray
        sum = 0
        n = len(arr)
        for i in range(n): 
            #storing prefix sum.
            sum += arr[i] 
            if sum == 0 or sum in s: 
                return True
            s.add(sum) 
        
        return False 
        
        
    def RowSum(self, row , mat, left , right):
        
        _sum = 0 
        
        for i in range(left , right+1) :
            _sum +=  mat[row][i]
            
        return _sum 
            
        
        
        
    def maximumSumRectangle(self,R,C,mat):
        #code here
        INT_MIN = -9999999999
        max_sum = INT_MIN
        
        
        for left in range(C):
            temp = [0]*R
            for right in range(left ,C):
                
                #here we can use RowSum function 
                # but this is better approach than that.
                for i in range(R):
                    temp[i] += mat[i][right]
                    
                max_sum =  max(max_sum , self.SubArraySum0(temp))
                    
        return max_sum 