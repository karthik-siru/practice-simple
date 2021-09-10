#question : 
'''
You are given a list of integers piles and an integer k. 
piles[i] represents the number of bananas on pile i. 
On each hour, you can choose any pile and eat r number of bananas in that pile. 
If you pick a pile with fewer than r bananas, it still takes an hour to eat the pile.

Return the minimum r required such that you can eat all the bananas in 
less than or equal to k hours.
'''

#approach : 
'''
->  The idea is to use binary-search .. let's first find the searh-space of the r 
->  Min speed needed is 1 
->  Whereas max_speed is max(piles).. because if it spends max time on it 
->  Now let's write a check function, and do a binary-search.  
'''


class Solution:
    # check function with speed r 
    def isPossible(self, piles , r, k) : 
        hours = 0

        for i in piles : 
            hours += i//r 
            if i%r : 
                hours += 1 
            # no need  to check , if it croses k      
            if hours>k : 
                return False 

        return hours <= k


    def solve(self, piles, k):
        # set the limits 
        left = 1
        right = max(piles)
        INF = 9999999
        min_speed = INF
        # binary-search:
        while left <= right : 
            mid = (left + right)//2 
            if self.isPossible(piles, mid , k) : 
                min_speed = min(mid , min_speed)
                right =  mid -1 
            else : 
                left =  mid + 1 

        return min_speed

        