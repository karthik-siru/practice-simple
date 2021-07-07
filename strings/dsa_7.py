
'''
Algorithm  :
   
    So , the longest palindrome , will start in the middle . So , the key idea is to 
    to find the longest palindrome , with  ith  index as center . and to cover the even 
    length strings we , run the expand fundtion with ith index and i+1 th index as center 
    

Note :
   This approach is better  than Dynamic programmming approach because , we don't use 
     extra space here . 

'''


class Solution:
    
    def expand (self, s, left, right ) :
        n = len(s)
        
        while left >= 0  and right < n   and s[left] == s[right] :
            left -= 1 
            right +=  1
            
        return s[left+1 : right ]
        
    def longestPalin(self, S):
        # code here
        
        if  S == "" :
            return 0 
        longest = ""
        
        for i in range(len(S)) :
            
            p1 =self.expand(S, i-1 , i+1 )
            
            if len(p1) > len(longest) :
                longest  =  p1 
                
            p2  =  self.expand(S, i , i +1 )
            
            if len(p2) > len(longest):
                longest  = p2 
                
        return  longest