def AggCows(self,arr, n, m):
    # function to check the possibility of division.
    def placeCows(barrier ) :           
        cows= 1  
        cord = arr[0]        
        for i in arr : 
            if i-cord >= barrier : 
                cows += 1 
                cord = i
        if cows >= m : 
            return True 
        return False 

    #defining search-space 
    left, right = 1 , arr[-1] -arr[0]    
    res = -1 
    #binary search ..
    while left <= right : 
        mid = (left + right)>>1
        #if allocation possible.. check with
        # lower limits.
        if placeCows(mid) : 
            res =  mid 
            left =  mid +1  
        else : 
            right = mid -1 
        
    return res 

