#question : 
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

# approach : 
'''
->  Let's first get the row number 
->  Then do the binary-search in that row ;) 

'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        n =  len(matrix)
        m =  len(matrix[0])
        l , r = 0 , n-1 
        # get the row number 
        while l<=r : 
            mid = (l+r)//2 
            
            if matrix[mid][m-1] == target : 
                return True 
            elif matrix[mid][m-1] >  target : 
                r =  mid -1 
            else : 
                l = mid +1 
        # update row if necessary         
        if matrix[mid][m-1] < target  and mid < n-1  : 
            mid += 1 
        row =  matrix[mid]
        
        l, r = 0, m-1 
        #do binary-search in the row ... 
        while l<=r : 
            mid = (l+r)//2 
            if row[mid] == target :
                return True 
            elif row[mid] > target : 
                r =  mid -1 
            else : 
                l =  mid +1 
                
        return False 