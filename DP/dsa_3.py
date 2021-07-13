
'''
Idea :  maintain a 1D array which contains factorials . 

return the n!/ (n-r)! 

As simple as that .

'''

class Solution :

    def Permutation_coef (self, n , r) :

        fac =[1]*(n+1)

        for i in range(1,n+1) :
            fac[i] = i*fac[i-1]

        return int(fac[n]//fac[n-r])
