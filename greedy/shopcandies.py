#question : 
'''
In a candy store, there are N different types of candies available and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get at most K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to find what is the minimum amount of money you have to spend to buy all the N different candies. Secondly, you have to find what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.
'''

class Solution:

    def candyStore(self, candies,N,K):
        # code here
            
        min_val , max_val = 0, 0  
        i = 0
        k = N-1 
        
        candies.sort()
        
        while i <= k : 
            min_val += candies[i]
            k -= K
            i += 1 
        i = N-1 
        k = 0
        
        while i >= k : 
            max_val +=  candies[i]
            i-= 1 
            k += K
        return (min_val , max_val)