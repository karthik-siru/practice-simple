# Question : 
'''
Square of the number without using * multiplication . 
'''


'''
  square(n) = 0 if n == 0
  if n is even 
     square(n) = 4*square(n/2) 
  if n is odd
     square(n) = 4*square(floor(n/2)) + 4*floor(n/2) + 1 
'''

class Solution : 
    def square(self, n):
    
        # Base case
        if (n == 0):
            return 0
    
        # Handle negative number
        if (n < 0):
            n = -n
    
        # Get floor(n/2) using
        # right shift
        x = n >> 1
    
        # If n is odd
        if (n & 1):
            return ((self.square(x) << 2)
                    + (x << 2) + 1)
    
        # If n is even
        else:
            return (self.square(x) << 2)