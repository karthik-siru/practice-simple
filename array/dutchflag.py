# question :
"""

Given an array of strings .. "red", "green", "blue" 
Rearrange them such that red comes first, and then green and then blue 
"""

# My approach :
"""
-> Let's take two pointers .. one is left,and the other is right 
-> left points to the next element after all "red".
-> right points to the prev element before all "green"

->  We will iterate over the array .. and whenever we found 
   a) RED ... swap with left and increment left
   b) BLUE .. swap with right and decrement right 
   c) GREEN ... just leave it.

->  Exceptional Cases : 
   a) When we found red and iterator and left are at same index 
   b) When we found blue and iterator and right are at same index
"""


class Solution:
    def solve(self, strs):

        n = len(strs)

        left, right = 0, n - 1
        iterator = 0

        while iterator <= right:
            if strs[iterator][0] == "r":
                if iterator == left:
                    iterator += 1
                else:
                    strs[left], strs[iterator] = strs[iterator], strs[left]
                left += 1

            elif strs[iterator][0] == "b":
                if iterator == right:
                    break
                else:
                    strs[right], strs[iterator] = strs[iterator], strs[right]
                right -= 1
            else:
                iterator += 1

        return strs


# Editorial - Approach :
"""
->  First place all the reds in one place 
->  Now think about green and blue
->  We can extend this to any number of colours 

"""


class Solution:
    def solve(self, s):
        def partition(s, start, word):
            for i in range(start, len(s)):
                if s[i][0] == word[0]:
                    s[i], s[start] = s[start], s[i]
                    start += 1
            return start

        start = partition(s, 0, "red")
        partition(s, start, "green")
        return s
