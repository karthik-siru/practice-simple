#approach : 
'''
->  Let's define our search-space --> [0 to max(heights)]
->  Similar to booksAllocation ... we will proceed.
'''

class Solution:
    
    #Function to find minimum number of pages.
    def maxHeight(self,arr, m):
        # function to check the possibility of division.
        def isPossible(barrier) :   
            sum = 0
            for i in arr : 
                if i >barrier :
                    sum += (i-barrier)
                if sum >=m : 
                    return True 
            return False        
            
        #defining search-space 
        left, right = 0 , max(arr)
        
        res = -1 
        #binary search ..
        while left <= right : 
            mid = (left + right)>>1
            #if allocation possible.. check with
            # lower limits.
            if isPossible(mid) : 
                res =  mid 
                left = mid +1 
            else : 
                right = mid -1 
            
        return res 

if __name__ == "__main__" : 
    a =  Solution()
    n,m = [int(i)  for i in input().split()]
    arr = [int(i)  for i in input().split()]
    print(a.maxHeight(arr,m))