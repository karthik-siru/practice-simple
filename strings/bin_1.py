
'''
  Algorithm : 

       It is same as finding length of the balanced string already .

'''

class Solution:
    def solve(self, s):
        stack =[]
        res = ""
        for i in s :
            if i =='(' :
                stack.append('(')
            if i ==  ')' :
                if stack and stack[-1] ==  '(' :
                    stack.pop()
                    res += '()'
        return len(res)