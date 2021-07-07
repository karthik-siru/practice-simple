
'''
 Algorithm : 
 it is pretty straight forward , in say  function  run a loop to find the frequencies 
 of the adjacent repeating elements. 
 

'''

class Solution(object):
    
    def say (self, s) :
        
        i = 0
        res = ""
        
        while i < len(s):
            count = 1
            while  i < len(s)-1  and  s[i] == s[i+1]:
                count += 1
                i +=  1
                
            res += str(count ) + s[i] 
            i +=  1
            
        return res
            
        
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # plan annd write the code ra  ...
        
        # base case :   if n == 1  : just return "1"
        
        # else  return say ( count_annd_say ( n-1 ) )  
        
        
        if n ==  1 :
            return  "1" 
        else :
            return  self.say(self.countAndSay(n-1))