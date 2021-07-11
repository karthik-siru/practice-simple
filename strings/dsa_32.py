
'''
Idea : 
  We will use sliding window technique to solve the problem . we mmaintain two pointers 
  i(back) and j(front)  

  -> whenever we didn't encounter all the distinct elements we increment j 
  -> when we found one , we just increment i  and (stores the minimum string length so far). 

'''

class Solution:
    def findSubString(self, string ):
        # Your code goes here
        n =  len(string) 
        if n <2 :
            return n 
            
        s =  len(set(string))
        i, j , minimum = 0, 1 , n
        while j <= n :
            if len(set(string[i:j])) ==  s :
                minimum = min(minimum , j-i)
                i += 1 
            else :
                j +=  1 
        return minimum 