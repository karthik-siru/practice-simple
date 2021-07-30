'''

Find the first and last occurence of the element in a sorted array .

'''

def find(arr,n,x):
    # code here
    
    l = 0 
    r =  n-1 
    
    init , end = -1 , -1 
    
    while l <= r :
        mid = (l+r)//2 
        
        if arr[mid] == x :
            init = mid 
            r =  mid -1  
            
        elif arr[mid ] < x :
            l = mid +1 
        else :
            r =  mid -1 
            
    l , r =  0 , n-1 
            
    while l <= r :
        mid = (l+r)//2 
        
        if arr[mid] == x :
            end = mid 
            l = mid +1  
            
        elif arr[mid ] < x :
            l = mid +1 
        else :
            r =  mid-1 
        
            
    return (init , end )