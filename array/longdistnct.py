# question :
"""
->  Given an array .. return the length of the longest sub-array , with distinct numbers .

Ex: [2,2,3,4,1,2,2,2,2,4]  -->  4 
"""


# approach :
"""
->  Let's do it with sliding window technique. 
->  Let's take two pointers ,, left and right and let's maintain a set 
->  and two variables .. which tracks lengths and max_lengths.. 
->  Every time we saw  a new element .. which is not in set .. append it to the set and 
    increment the length and max_length . and move the right pointer 
->  If the element is already in the set .. move the left pointer to the next index of the 
    found element in the current subarray 
->  return max_length 
"""


class Solution:
    def solve(self, nums):

        if not nums:
            return 0

        s = set()

        i, j = 0, 0
        max_length = 0
        length = 0
        n = len(nums)

        while j < n and i <= j:
            if nums[j] not in s:
                # add to the list &
                # update lengths.
                s.add(nums[j])
                length += 1
                max_length = max(max_length, length)
                j += 1
            else:
                # move the left untill the found element
                while i <= j:
                    if nums[i] == nums[j]:
                        length -= 1
                        s.remove(nums[i])
                        i += 1
                        break
                    # update length and remove b/w elements
                    length -= 1
                    s.remove(nums[i])
                    i += 1

        return max_length

