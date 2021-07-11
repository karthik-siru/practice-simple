'''
 Idea :  three length palindromes must contains the first and last character .

 -> So ,let's search for the characters from the front and from the back .
 -> if front < back , then 
 -> number of palindromes are equal to numbber of unique letters between the 
    front and back indices . 

'''


class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        n =  len(s)
        count = 0
        l = set(s)
        for i in l :
            front =  s.find(i)
            back =  s.rfind(i)
            if front < back :
                count  +=  len(set(s[front+1 : back]))
                
        return count 
        