#approach : 
'''
->  What is the min a person can get -->  that is min(arr)
->  What is the max a person can get -->  that is sum(arr)

-> these two are the limits for our search space ..  
-> Suppose we want the mid value of both these limits as our answer 
-> we have to make sure that no person can get more than this .

-> Allocate all the values to the first person ..untill the pages are less than mid
-> if it had cross the mid .. start giving pages to the second and soon.

-> Finally , if the student count >k return False 
-> Else .. true 

'''

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,arr, n, m):
        # function to check the possibility of division.
        def allocationpossible(barrier ) :           
            students , pages = 1, 0             
            for i in arr : 
                if pages + i > barrier : 
                    pages = i
                    students += 1 
                    # not possible to have a low barrier
                    if pages >  barrier : 
                        return False 
                else : 
                    pages += i 
            if students <= m : 
                return True 
            return False 
        #defining search-space 
        left, right = min(arr) , sum(arr)
        
        res = -1 
        #binary search ..
        while left <= right : 
            mid = (left + right)>>1
            #if allocation possible.. check with
            # lower limits.
            if allocationpossible(mid) : 
                res =  mid 
                right = mid -1 
            else : 
                left = mid +1 
            
        return res 