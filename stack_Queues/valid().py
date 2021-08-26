#question :  
'''
->  Given a string consists of only ( and ) .. return the length of the 
    longest valid paranthesis . 

'''

# Thoughts : 
'''
->  Map (  with  1 and ) with -1 ... now our job becomes simple .. to find the 
    max subarray of length with sum 0  
->  Brilliant right ... but  think of this  case ")(" .. this will also
    considered as valid according to previous idea 
->  So, This approach is wrong 
'''

# Approach : 
'''
->  whenever we find ) , we need the index of ( to previous of tha. 
->  We will store the indices  of ( in a stack 
->  Whenever we find ) we pop from the stack and calculate the length ..
->  Note that... top value of the stack .. when we find ) are valid ;) 
->  Whenever the stack becomes empty .. we will push the current index.
->  We start with pushing -1 to the stack .  
->  To handle ... ) just after valid paranthesis... 
'''


class Solution : 

    def ValidString(self, s):

        max_length = 0
        stack = []
        # this is for ) after valid string 
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(' :
                stack.append(i)
            else : 
                top =  stack.pop()
                # if stack becomes empty 
                # append the current value 
                if not stack : 
                    stack.append(i)
                else : 
                    max_length = max(max_length, i-top )

        return max_length 

