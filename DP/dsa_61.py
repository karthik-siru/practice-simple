'''
Idea :  maintain an array , which stores the max profit with i length at ith index.

'''

class Solution :
    def rod_cutting (self, n , arr):
        res = [0]*(n+1)

        for i in range(1, n+1) :
            j = 0 
            while j <i :
                res[i]  = max(res[i], arr[j] + res[i-j-1])
                j +=  1
        return res[-1]