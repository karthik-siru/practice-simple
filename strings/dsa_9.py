'''
Algorithm :

   We used pick and not pick method. when there is nothing input ,we just print the 
   output , and we recursively choose to pick and not to pick 
'''



class Solution :

    def print_all_subsequence (self, s , output ) :

        if s == "" :
            print(output)
            return 
        
        self.print_all_subsequence(s[1:] , output +s[0] )
        self.print_all_subsequence(s[1:], output )

a = Solution()
a.print_all_subsequence(input(), "")

