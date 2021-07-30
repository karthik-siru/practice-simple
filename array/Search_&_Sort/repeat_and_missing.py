'''
We used the same technique which we used to find the first missing positive number

to fins the repeatd number . 

-> to know the missing number, we used some simple maths ;) 

'''

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        
        array_sum =  sum(arr) 
        max_sum  =  n*(n+1)//2 
        
        repeat =  self.repeatedNumber (arr ,n )
        
        missing = max_sum - array_sum + repeat 
        
        return (repeat , missing )
        
        
    def repeatedNumber(self , arr , n ) :
        
        i = 0  
        
        while i < n : 
            
            if arr[i]  ==  i + 1 :
                i += 1 
            else :
                index = arr[i] -1 
                if arr[index] == index +1 :
                    return arr[index]
                else :
                    arr[i] , arr[index]  = arr[index] , arr[i]