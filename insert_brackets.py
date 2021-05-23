'''
Given a string s containing brackets ( and ), return the minimum number of brackets 
that can be inserted so that the brackets are balanced.


Example 1
Input

s = ")))(("

Output

5

Explanation

We can insert ((( to the front and )) to the end

'''

'''
  The minimum number of brackets to be inserted is also the number of brackets to close on the right plus the number of brackets to open on the left.

We can use a right  that keeps track of how many open parenthesis should be closed. If we see a closing bracket while our stack is empty, we add one to a counter, this counter represents the number of brackets to open on the left.

Adding the counter and the right  gives the result.

  
'''



class Solution:
    def solve(self, s):
        left = 0
        right = 0

        for i in s:
            if not right and i == ')':
                left += 1
            elif i == '(':
                right += 1
            else :
                right -= 1
        return left+righ
