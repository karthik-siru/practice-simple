
#question : 
'''
You are given N pairs of numbers. 
In every pair, the first number is always smaller than the second number.
A pair (c, d) can follow another pair (a, b) if b < c. 
Chain of pairs can be formed in this fashion. 
You have to find the longest chain which can be formed from the given set of pairs. 

'''

#example : 
'''
Input:
N = 5
P[] = {5  24 , 39 60 , 15 28 , 27 40 , 50 90}
Output: 3
Explanation: The given pairs are { {5, 24}, {39, 60},
{15, 28}, {27, 40}, {50, 90} },the longest chain that
can be formed is of length 3, and the chain is
{{5, 24}, {27, 40}, {50, 90}}
'''

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

class Solution : 

    def maxChainLen(Parr, n):
        # Parr:  list of pair
        #code here
        # sort the pairs according to their finishing time
        Parr.sort(key =  lambda x : x.b )
        # set count to 1 and deadline
        count = 1
        deadline = Parr[0].b
        
        i = 1 
        # if the next work is after deadline
        #  allocate the process.
        while i <  len(Parr) : 
            if Parr[i].a >  deadline : 
                count += 1 
                deadline =  Parr[i].b 
            i += 1 
                
        return count 
