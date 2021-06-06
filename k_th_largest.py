
'''

k th largest / smallest element in the given array .. 

Idea :: Selection-Sort 

'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range (k ) :
            largest = i 
            
            for j in range (i+1, len(nums)) :
                if nums[j] > nums[largest] :
                    largest = j 
            nums[largest] , nums[i] = nums[i] , nums[largest]
            
        return nums[k-1]
