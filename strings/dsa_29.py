
class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        balance = 0 
        swap_count = 0
        left_count , right_count = 0, 0 
        i = 0
        
        
        while i < len(S) :
            if S[i] == '[' :
                left_count +=  1
                
                if balance > 0 :
                    swap_count +=  balance 
                    balance -=  1 
            else :
                right_count += 1 
                balance =  right_count- left_count 
                
            i += 1 
                
                    
        return swap_count 