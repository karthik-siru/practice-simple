#approach : 
'''
Given an array of numbers , where each nnumber is repeated thrice , except one .
Find that number ..

'''

#approach : 
'''
For every bit (suppose it's a 32 bit integer) 
we can count the number of elements who have this bit set, 
since every number except the lone integer integer is repeated thrice 
so the count of elements at a particular bit should be divisible by 3,
otherwise it means that this bit is set in the lone integer.
'''

class Solution:
    def solve(self, nums):
        ans = 0
        for i in range(32):
            bit = 0
            for j in nums:
                if j & 1 << i:
                    bit += 1

            if bit % 3 == 1:
                ans |= 1 << i
        return ans
