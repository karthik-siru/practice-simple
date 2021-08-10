# Question : 
'''
Number of triplet pairs , whose sum is less than the target. 
'''

#Approach : 
'''
First , let's sort the array, 
Now for each element , let's find the two sum count of target-element in the 
remaining array ;) 


->  How to know the  pairs of two sum in sorted array  :

->  if left + right <  target ->  all the numbers b/w left and right are also valid 
->  if left + right >= target ->  decrease the sum , i.e right -= 1 .  

'''


class Solution:

    def countTriplets(self, nums, n, sumo ):
        #code here
        

        # returns the count of pairs whose sum < target in sorted arra.
        def twosumcount (left , right , target ) : 
            count =0
            while left < right : 
                sum =  nums[left] +  nums[right]
                # target is greater than  sum .. decrease sum ;) 
                if sum >= target : 
                    right -= 1 
                else : 
                    count += right- left 
                    left +=1    
            return count 
            
        nums.sort()
        
        count = 0 
        
        for i in range(len(nums)): 
            
            num =  nums[i]
    # search for pairs in remaining array with target as (target - num )
            count += twosumcount(i+1 , len(nums)-1 , sumo - num )
                
        return count 