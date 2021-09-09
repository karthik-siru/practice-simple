# question :
"""
Given an integer array nums, you need to find one continuous subarray that if you only 
sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.


"""

# approach :
"""

->  See the image linked to this question. 

-> The plan is to find the start and end of the continous array . 

->  Look at the graph ... we just need to find the smallest index , where the slope drops 
    for the start of the array 

->  To find the end of the subarray , we need to find the greatest index , where the slope 
    rises again 

"""


class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:

        start, end = -1, -1

        prevHigh = len(nums) - 1
        prevLow = 0
        # to find the end
        for i in range(len(nums)):
            if nums[i] < nums[prevLow]:
                end = i
            else:
                prevLow = i
        # to find the start
        for i in reversed(range(len(nums))):
            if nums[i] > nums[prevHigh]:
                start = i
            else:
                prevHigh = i

        if start >= 0 and end >= 0:
            return end - start + 1
        return 0

