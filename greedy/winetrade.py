
#approach : 
'''

Locate the leftmost seller and send as much wine as possible/required to the first buyer.
If the seller does not have any wine left after this,
move on to the next seller. 
Alternately, if the buyer requirement has been met, 
move on to the next buyer. Keep doing this till all wine has been moved 
from the sellers to the buyers. Since the house locations have been 
already provided in sorted order, this can be done in O(N).
'''
class Solution : 

    def wineTrade(self, n , a ):
        res = 0
        buyer , seller = 0, 0  

        while 1 :
            while seller!= n and a[seller] < 0 :
                seller +=1 
            while buyer != n and a[buyer] > 0:
                buyer +=1 
            if buyer == n and seller == n : 
                break 
            transaction =  min(a[buyer] , -a[seller])
            res += transaction
            a[seller] += transaction
            a[buyer] -=  transaction

        return res 
