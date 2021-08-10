'''
 Given the starting number(A) and difference(C) . Say whether B is in the 
 Arthematic Progression or not ? 

'''

# Approach : 
'''
We can simply think that , (B-A)%C == 0 .. but think of this example .  

A = 4 , B = 0 , C = 4 .. 
So we have to cover the edge cases first ;). 
'''

class Solution:
    def inSequence(self, A, B, C):
        # code here
        
        if (B> A and C <=0 ) or (B<A and C >= 0) :
            return 0
            
        if (B == A and C == 0) :
            return 1 
        
        return 1 if (B-A)%C == 0 else 0 