#question : 
'''
Given two sorted arrays .. sort them  without using extraa space ..  I mean at the end,
array1 + array2  -> sorted list of the numbers. 
'''

# Approach : 
'''
->  let's maintain two pointers .. i, j for two arrays 
->  If ith  element is less than jth element .. correct place (increment i)
->  else jth element deserves a place in the array1 
->  FOr that , we use a variable k to store last index of n-1 
->  Now we swap jth-element and kth element (increment j and decrement k)
->  Finally sort arr1 and arr2 . 
'''
class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        
        i , j , k  = 0 , 0, n-1 
        
        while i<= k and j < m : 
            
            if arr1[i] <  arr2[j] :
                i += 1 
            else : 
                arr2[j] , arr1[k] = arr1[k] , arr2[j]
                j +=  1
                k -=  1 
                
        arr1.sort()
        arr2.sort()