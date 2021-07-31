class Solution :

    # returns the maxlength subarray with given sum 
    def maxlengthSubarray(self, nums , target ) :
        
        # this stores the max_length found upto now.
        length = 0  

        hash_map =  {}
        
        # this is for the case , when the subarray ,starts from index 0
        hash_map[0]  = -1 
        endindex = -1 
        sum = 0 

        for i in range(len(nums)) :

            sum  += nums[i]
            
            # if sum is seen for the first time add it to the dict
            if sum not in hash_map :
                hash_map[sum] =  i 
            
            # imagine the target as 0  
            # so we will search whether the current sum  is already seen or not 
            # in the same way , we look for sum-target .
            if sum-target in hash_map and length < i - hash_map[sum-target] :
                endindex =  i
                length =  i - hash_map[sum -target]

        return length 