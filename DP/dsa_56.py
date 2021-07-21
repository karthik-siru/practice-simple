#qUESTION : 
'''
   Given a 2D mmatrix, Find sub-rectangular matrix with maximum sum .
'''


'''
Idea :  
        -> fix the left limit and the right limit for the matrix .
        -> Now calculate the row-wise sum for all the rows from left to right 
        -> store the row-wise sums in an array temp,
        ->  Now aply the "Kadane's Algorithm " for the temp 
        ->  Keep track of the max_value so far ;)
        * Amazing isn't it ;) 

'''


class Solution: 
    
    def KadaneAlgo(self,a):
        INT_MIN =  -99999999999
        global_max  = INT_MIN
        local_max = 0
        
        for i in a :
            
            local_max =  max(i , i + local_max)
            
            if local_max > global_max :
                global_max =  local_max 
                
        return global_max 
        
        
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
                    
                max_sum =  max(max_sum , self.KadaneAlgo(temp))
                    
        return max_sum 