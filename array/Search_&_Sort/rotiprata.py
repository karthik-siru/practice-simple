#approach : 
'''
->  k ... p*(p+1)//2 
->  What is the min time -->  k
->  What is the max time -->  8*k

-> these two are the limits for our search space ..  
-> Suppose we want the mid value of both these limits as our answer 
-> we have to make sure that no chef can get more time  than this .

-> Allocate time to the first chef ..untill time is less than mid 
-> if it had cross the mid .. start giving time to second chef 

-> Finally , if the parata count >m return True 
-> Else .. False  

'''


class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,arr,p):
        # function to check the possibility of division.
        def allocationpossible(barrier ) :           
            paratas = 0         
            for i in range(len(arr)): 
                c = 0
                time =  mid 
                perparota = arr[i]
                while time : 
                    time -= perparota
                    c += 1 
                paratas += c 
                if paratas >= p : 
                    break
            if paratas >= p : 
                 return True 
            return False 
            
        #defining search-space 
        k = p*(p+1)//2 
        left, right = k , 8*k
        
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