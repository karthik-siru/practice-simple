'''
  If you try to maintain a count and increment and decrement whenever we encounter an open and 
  closed paranthesis will give you wrong answer , because 

  Think of this testcase --> '}{'

  So, we have to check while decrementing , whether the count is 0 or not . 

'''

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        s,r,f = 0 , 0 , 0 
        
        for i in x :
            if i == '[' :
                s += 1
            if i == ']':
                if s == 0:
                    return False
                else :
                    s -= 1
            if i == '('  :
                r += 1
            if i == ')':
                if r == 0:
                    return False
                else :
                    r -= 1
            if i == '{'  :
                f += 1
            if i == '}':
                if f == 0:
                    return False 
                else :
                    f -= 1
                
        if not s and not r and not f :
            return True 
        else :
            return False 