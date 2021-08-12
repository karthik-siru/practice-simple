#question : 
'''
Given an array A[ ] of positive integers of size N,
where each value represents the number of chocolates in a packet.
Each packet can have a variable number of chocolates. 
There are M students, the task is to distribute chocolate packets 
among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates 
   given to a student and minimum number of chocolates
   given to a student is minimum.

'''

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        
        A.sort()
        i , j  = 0  , M-1 
        min_dif = 9999999999999 
        while j < N :
            if (A[j] - A[i] ) < min_dif :
                min_dif = A[j] - A[i]
            j += 1
            i+= 1 
        return min_dif 