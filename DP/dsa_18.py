
'''
Same as the Longest increasignsubsequence , but some slight 
variation  ;) 

->  Self explanatory 

'''

class Solution:
    def maxSumIS(self, a, n):
        # code here
        
        lis = [0]*n 
        
        lis[0] = a[0]
        
        for i in range (1,n) :
            lis[i] = max(lis[i], a[i])
            for j in range(i):
                if a[j] < a[i] :
                    lis[i] =  max(lis[i], lis[j]+a[i])
                    
        return max(lis)