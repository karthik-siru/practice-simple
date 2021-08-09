'''
Given an array of elements , with max diff b/w adj elements  be k . 
Ex : 
   [4 , 5, 6, 7, 6, 5]

'''

# Approach : 
'''
 We can simply do a linear search and find our required element . 

 ->  we can optimise it better by utilising the array property.  
 ->  let we want to find the element x , and current element is a 
 ->  let their abs diff b/w  x and a is  diff . 

 ->  Instead of jumping one step , we can jump diff/k steps at once ;) 

'''

class Solution : 

    def searchArraydifk(self, arr, key, k ) :
        n =  len(arr)
        
        index  = 0 

        while index  < n : 
            if arr[index] ==  key : 
                return index 

            index  +=  max( 1, int(abs(arr[index] - key)//k)) 

        print(f"element {key} not found in the array ")
        return -1 

        