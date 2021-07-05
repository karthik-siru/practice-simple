'''

                                 ABCD 
                                  |
                 ABCD     BACD         CBAD  DBCA   ( swap A with all the characters )
                  | 
            ABCD  ACBD   ADCB  (Now leave A and do the same for B )

            and the recursion continues 



Psuedo-Code  :

   permutation (s, l , r) :
      
      for i in range (l, r+1):
         swap (s+l , s + i)
         permutation(s, l+1, r)
         swap (s+l, s+ i)

'''


class Solution:
    def find_permutation(self, S):
        # Code here
        
        res = set()
        
        def print_perm (s, left , r , res ) :
            if s == "" :
                return 
            
            for i in range(left , r+1 ) :
                
                l = list(s) 
                l[i] , l[left]=  l[left] , l[i]
                s = ''.join(l)
                res.add(s)
                print_perm(s, left+1, r , res ) 
                l = list(s) 
                l[i] , l[left]=  l[left] , l[i]  
                s = ''.join(l)
                
            
        print_perm (S, 0 , len(S)-1 , res )
        
        return sorted(list(res)) 
            