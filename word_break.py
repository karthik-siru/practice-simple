
'''

Not efficient way .. but gives the solution 

'''

class Solution:
    def solve(self, words, s):
        if s ==  "":
            return True 
    
        i = 0
        while  i <= len(s):
            if s[:i]  in words :
                if self.solve(words , s[i:]) :
                    print(f'back to the function with string {s}')
                    return True 
                 
            i += 1

        return False
