#question :
'''
You are given a list of integers nums. Return the number of pairs i < j such that nums[i] = nums[j].

Constraints

0 ≤ n ≤ 100,000 where n is the length of nums
'''

class Solution:
    def solve(self, nums):

        if len(nums) < 2 :
            return 0 

        hash = {}

        for i in nums : 
            hash[i] = hash.get(i, 0) + 1 
        count = 0 
        for i, j in hash.items():
            count += j*(j-1)//2 

        return count 
        