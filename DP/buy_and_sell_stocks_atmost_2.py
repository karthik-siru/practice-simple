'''

Best time to buy and sell stocks  with atmost 2 transactions .. 

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        hold = [-float('inf')]*2
        not_hold = [0]*2
        
        for i in prices :
            
            not_hold[1] =  max(not_hold[1] , hold[1] + i)
            hold[1]  =   max(hold[1] , not_hold[0] - i)
            
            not_hold[0] = max(not_hold[0] , hold[0] + i )
            hold[0] = max(hold[0] , 0 -i )
            
            
        return not_hold[-1]
      
      
      
'''

with generalised atmost k transactions 

'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B ==0   or len(A) < 1 :
            return 0 
        hold = [-float('inf')]*B
        not_hold = [0]*B
        
        for i in A :
            j = B-1
            while j > 0 :
                not_hold[j] = max(not_hold[j] , hold[j] + i )
                hold[j] = max(hold[j] , not_hold[j-1] - i)
                j -= 1 
            not_hold[0] = max(not_hold[0] , hold[0] + i )
            hold[0] = max(hold[0] , 0 - i)
            
        return not_hold[-1]
