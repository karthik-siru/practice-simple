
'''
Idea :  included in the code , this is for atmost 2 transactions , 

for generalised , atmost k transactions look below this code .

'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
            '''
            dp_2_hold: max profit with 2 transactions, and in hold state
            dp_2_not_hold: max profit with 2 transactions, and not in hold state
        
            dp_1_hold: max profit with 1 transaction, and in hold state
            dp_1_not_hold: max profit with 1 transaction, and not in hold state
            
            Note: it is impossible to have stock in hand and sell on first day, therefore -infinity is set as initial profit value for hold state
            '''
            
            dp_2_hold, dp_2_not_hold = -float('inf'), 0
            dp_1_hold, dp_1_not_hold = -float('inf'), 0
            
            for stock_price in prices:
                
                # either keep being in not-hold state, or sell with stock price today
                dp_2_not_hold = max( dp_2_not_hold, dp_2_hold + stock_price )
                
                # either keep being in hold state, or just buy with stock price today ( add one more transaction )
                dp_2_hold = max( dp_2_hold, dp_1_not_hold - stock_price )
                
                # either keep being in not-hold state, or sell with stock price today
                dp_1_not_hold = max( dp_1_not_hold, dp_1_hold + stock_price )
                
                # either keep being in hold state, or just buy with stock price today ( add one more transaction )
                dp_1_hold = max( dp_1_hold, 0 - stock_price )
                
            
            return dp_2_not_hold


    # for generalised amost k transactions. 


    def maxProfit(self, B, N, A):
        # code here
        
        if B ==0  or len(A) < 1 :
            return 0 
        hold = [-float('inf')]*B
        not_hold = [0]*B
        
        for stock_price in A :
            j = B-1
            while j > 0 :
                not_hold[j] = max(not_hold[j] , hold[j] + stock_price )
                hold[j] = max(hold[j] , not_hold[j-1] - stock_price)
                j -= 1 
            not_hold[0] = max(not_hold[0] , hold[0] + stock_price )
            hold[0] = max(hold[0] , 0 - stock_price)
            
        return not_hold[-1]
