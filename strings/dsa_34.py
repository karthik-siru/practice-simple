
'''
Algorithm :  
    We use the kmp preprocessing algorithm to solve this pproblem . 

    we make a string ->  string +  special_character + reverse of the string .

    and apply the longest prefix and suffix problem  ... 


   #  Why special character  :
      
         Thiis is to make sure that ,LPS at $ should become 0 and we start from reverse of string.

'''

from dsa_18 import Solution

def add_in_the_beginning(s):
        rev  =  s[::-1]
        sc  =  '$' 

        s =  s + sc +rev  
        self = 'a'
        lps = Solution.lps(self, s)
        return lps[-1]

s =  input('enter the string ')

n =  add_in_the_beginning(s)
print(f'Number of characters added in the front to make  string palindrome is {len(s)-n}')