
'''
  Algorithm : 
      
      So keep a stack , if it is '}' and top the stack is '{' , pop the element
      if it is '{'  ppush it into the stack  . 

      After traversing the stack , the number of open  -> n annd closed -> m 

      the result is  ceil(n/2)  + ceil(m/2) .

      Instead of  using the stack , we can do it by using two variables (as given below)

'''

class Solution :
    def countRev (s):
        # your code here
        
        if len(s)%2 :
            return -1 
        
        left , right  = 0 , 0 
        
        for i  in s :
            if i  == '{' :
                left +=  1
            else :
                if left == 0 :
                    right +=  1
                else :
                    left -=  1
        if left%2 :
            left += 1
        if right%2 :
            right  +=  1
        left =  left//2 
        right =  right//2 

        
        return left + right 