# question :
"""
Given an array Arr of size N such that each element is from the range 0 to 9. 
Find the minimum possible sum of two numbers formed using the elements of the array. 
All digits in the given array must be used to form the two numbers.
"""


# approach :
"""
-> So we have to form two average numbers ( coz we can't reuse numbers )
-> So first let's sort the elements of an array , and distribute the elements 
"""


class Solution:
    def solve(self, arr, n):
        # code here

        arr.sort()

        even = 0
        odd = 0

        for i in range(n):
            if i & 1:
                odd = odd * 10 + arr[i]
            else:
                even = even * 10 + arr[i]
        return odd + even

