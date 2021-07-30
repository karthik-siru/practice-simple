'''
Pivot :  See the attached picture to get the logic of finding pivot .

'''

class Solution:
    def search(self, nums, target: int) -> int:
        
        
        if not nums :
            return -1 
        
        n =  len(nums)
        
        pivot =  self.pivot(nums) 
        
        left =  self.binarySearch(nums , 0, pivot-1 , target ) 
        
        if left != -1 :
            return left 
        right =  self.binarySearch(nums , pivot , n-1 , target )
        
        if right != -1 :
            return right 
        
        return -1 
        
    
    # this function returns the index of pivot +1 
    def pivot (self, nums) :
        
        compare_element = nums[-1]
        
        l , r = 0 , len(nums)-1 
        
        while l <= r :
            
            mid =  (l+r)//2 
            
            if nums[mid] > compare_element :
                l = mid +1 
            else :
                r = mid -1 
                
        return l 
    
    def binarySearch (self, nums , l , r , target ) :
        
        while l <= r :
            mid =  (l+r)//2 
            
            if nums[mid] == target :
                return mid 
            elif nums[mid] > target :
                r =  mid -1 
            else :
                l =  mid +1 
                
        return -1 