#question :
'''
Given two numbers .. return how many bits to be flipped to change to another number.
'''

#approach : 
'''
->  just count number of set bits in a^b. 
'''

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ##Your code here
        
        def count (n) :
            count = 0
            while n :
                n = n&(n-1)
                count +=1 
                
            return count 
            
        return count(a^b)
