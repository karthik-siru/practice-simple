#Question : 
'''
return an array  , which contains productt of all the elements in the array 
except itself.
'''

#Approach : 
'''
Keep track of two pointers ..one from the front and from the back .
-> Initialise all the values in result array with 1 
-> Keep on multiplying numbers for front and back 
-> Front will give the mulltiplication of all the numbers infront of them.
-> siimilarly back .  
'''

class Solution:
    def productExceptSelf(self, nums, n):
        #code here
        
        res = [1]*n
        f , b = 1,1
        
        for i in range(n):
            res[i] *= f 
            res[n-i-1]*= b 
            f *= nums[i]
            b *= nums[n-i-1]
            
        return res 