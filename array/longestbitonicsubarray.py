
# for subsequence , find the longest increasing  and decreeasing subsequence 


class Solution : 

    def longestBitonicSubarray (self, nums ) :
        
        n =  len(nums)
        # I --> Increasing subarray 
        # D --> Deccreasing subarray 
        I =  [1]*(n)
        
        # find the longest increasing subarray ending in the given index 
        for i in range(1,nums):
            if nums[i - 1] < nums[i]:
                I[i] = I[i - 1] + 1

        D = [1]*(n)
        
        # find the longest decreasing subarray starting from each index 
        for i in reversed(range(n-1)) :
            if nums[i] > nums[i+1] :
                D[i] = D[i+1]-1 

        max_val =  1 
        
        # find the max value of both of them ;) combined 
        for i in range(n) :
            max_val =  max(max_val , I[i]+D[i]-1 )

        return max_val 

