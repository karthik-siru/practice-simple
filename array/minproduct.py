#question : 
'''
You are given a positive integer p. Consider an array nums (1-indexed) that consists of the integers in the inclusive range [1, 2p - 1] in their binary representations. You are allowed to do the following operation any number of times:

Choose two elements x and y from nums.
Choose a bit in x and swap it with its corresponding bit in y. Corresponding bit refers to the bit that is in the same position in the other integer.
For example, if x = 1101 and y = 0011, after swapping the 2nd bit from the right, we have x = 1111 and y = 0001.

Find the minimum non-zero product of nums after performing the above operation any number of times. Return this product modulo 109 + 7.

Note: The answer should be the minimum product before the modulo operation is done.
'''

#approach : 
'''
  We must always try to make the number equal to 1 . ;) 
  ->  when we try that .. one number will be 1 and the other will be 2**p-2 
  ->  one extra element will also be there .. that is 2**p -1 

'''

class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        if p  == 1 : 
            return 1 
        
        MOD = 1000000007
        
        res = pow(pow(2, p, MOD) - 2, pow(2, (p - 1)) - 1, MOD) * (pow(2, p, MOD) - 1)
        return int(res) % MOD