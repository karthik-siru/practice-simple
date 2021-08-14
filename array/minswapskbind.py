#question : 
'''
 Given an array of n positive integers and a number k.
 Find the minimum number of swaps required to bring all the numbers 
 less than or equal to k together.
'''

#approach : 
'''
->  let's first count the number of elements in the array less than or equal to k
->  let's this count be windowsize .
->  Let's use sliding window to know the no. of numbers to be shifted..
->  And let's find the min swaps from that ;) 

'''

class Solution : 

    def minSwapsMethod1(self, arr , n , k):
        window  = 0
        for i in arr : 
            if i <= k  : 
                window += 1
        # returns no. of elements <= k i window
        def count (i, j ) :
            count = 0
            while i<= j : 
                if arr[i] <= k : 
                    count +=1                     
                i += 1                   
            return count 
            
        i = 0 
        j = i + window -1 
        inf = 9999999
        res =  inf 
        while j < n :            
            res =  min(res , window - count(i, j ))           
            j +=  1 
            i +=  1 
            
        return res 
# let's try to optimise it  ;)
'''
->  Each time we move our sliding window by 1 , we don't actually need to count 
    the bad numbers all again .
->  we can just update by just comparing the jth index number only.
->  update the final result after every move ... that's it 
->  Cool right 
'''
def minswapsMethod2 (self, arr , n , k ): 
        # number of elements <=  k 
        windowsize = 0 

        for i in arr : 
            if i<= k :
                 windowsize += 1 
        bad = 0 
        for i in range(0,windowsize) :
            if arr[i] >  k : 
                bad += 1 
        ans = bad 
        j = windowsize
        # current window is from [0 to windowsize-1]
        for i in range(0, n) :
            if j == n :
              break 
            # update previous window 
            if arr[i] > k : 
                bad -=  1
            # update for new window 
            if arr[j] > k : 
                bad += 1 
            # update the final result 
            ans =  min(ans , bad)
            j +=  1
        return ans 