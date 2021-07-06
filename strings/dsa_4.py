
'''

Algorithm : 
     
    1. Create a variable containing s1+s1 
    2. Now check whether s2 is substring of s1 or not ;)

    a.count(b) --> returns how many times b appeared in a 
     
'''

class Solution :

    def rotate_string (self, s1, s2 ) :

        if len(s1)!=  len(s2) :
            return False
        temp = s1 +  s1 
        if temp.count(s2) > 0 :
            return 1 
        else :
            return 0 


a = Solution()
print(a.rotate_string(input(), input()))