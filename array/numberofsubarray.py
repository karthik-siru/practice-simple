class Solution:
    def solve(self, nums, target):
        count = 0  

        hash_map =  {}
        
        sum = 0

        for i in range(len(nums)) :

            sum  += nums[i]
            
            if sum == target :
                count += 1 
            
            if sum-target in hash_map : 
                count   += hash_map[sum-target]

            if sum not in hash_map :
                hash_map[sum] = 1 
            else :
                hash_map[sum] +=  1

        return count 
        