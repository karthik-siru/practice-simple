'''
If you come up with complex idea like ->  for r singles ->  nCr *(n-r C 2)

Bro , think in recursive way ;) 

for nth person , there are two pssibilities : 

 1)  stay  single (like me ;) )then we have to deal with remaining n-1 peeps.
         i.e  ->  f(n-1)
 2)  paired , then we have to find a match for him  and deal with n-2 peeps
        founding pair can be done in n-1 ways 
        i.e  -> (n-1)*f(n-2)

     Total number of ways ->  stay single +  paired 
                         ->  f(n-1) + (n-1)*f(n-2)

    Since at each step we need only previous two values(no need to whole array).

'''

class Solution:
    def countFriendsPairings(self, n):
        # code here 
        
        a, b, c = 1, 2, 0;
        if (n <= 2):
            return n;
        for i in range(3, n + 1):
            c = b + (i - 1) * a;
            a = b;
            b = c;
        return c;