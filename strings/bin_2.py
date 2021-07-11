
'''
Idea  :
   the key takeaway from this question is that , if a string(s1) is rotation of 
   other(s2) , then the s1 must bbe substring of concatenation of s1 with itself .

   We maintain a set to hold the values of concatenated strings ,and returns 
   it's length .

'''

class Solution:
    def solve(self, words):
        s = set()
        for i in words :
            found = 0
            for j in s :
                if i in j and len(i) == len(j)//2 :
                    found = 1
            if not found :
                s.add(i*2)
        return len(s)