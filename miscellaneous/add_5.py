'''
idea :  deal with negative and positive numbers seperately .

'''

class Solution:
    def solve(self, n):
         s =  str(n)
         i = 0
         added =1 
         if n < 0 : 
             while i in range (len(s)):
                 if s[i] <= '5' :
                     i += 1 
                 else : 
                     s =  s[:i]+'5' +s[i:]
                     added =0 
                     break
             if added : 
                 s = s + '5'
             return int(s)

         else  : 
             while i in range (len(s)):
                 if s[i] >='5' :
                     i += 1 
                 else : 
                     s =  s[:i]+'5' +s[i:]
                     added =0 
                     break
             if added : 
                 s = s + '5'
             return int(s)
            