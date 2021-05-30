class Solution:
    def isNumber(self, s: str) -> bool:
        
        def is_integer (n):
            try :
                k = int(n)
                return 1 
            except :
                return 0 
            
        def is_decimal(s):
            
            if 'inf' in s or 'Inf' in s :
                return 0 
            try :
                k = float(s)
                return 1
            except :
                return 0 
        if 'e' in s  or 'E' in s :
            if s[0].lower()== 'e' or s[-1].lower()=='e' :
                return False
            
            if 'e' in s :
                k = s.index('e')
            else :
                k = s.index('E')
                
            if is_integer(s[k+1:]) and is_decimal(s[:k]) :
                return True 
            else :
                return False 
        else :
            return is_integer(s) or is_decimal(s)
