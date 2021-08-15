#question : 
'''
You are given a 0-indexed array nums of distinct integers. 
You want to rearrange the elements in the array such that every element 
in the rearranged array is not equal to the average of its neighbors.
More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1,
(nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].
Return any rearrangement of nums that meets the requirements.
'''

#approach : 
'''
-> Sort the array 
-> IF two numbers are greater than an element, then the two numbers average will
   also be greater than that element.
-> Similarly for less than element ;) 

-> Keep two pointers .. one from start and other from middle .. 
-> Now take one element from mid and another from start .. starting from the mi.

->  Finally , we will be having the required array .

'''

class Solution:
    def rearrangeArray(self, nums ) -> list[int]:
        
        nums.sort()
        
        i = 0 
        n =  len(nums)
        mid =  n//2  
        j = mid         
        #resultant array 
        res = []
        check = 1 # check for toggling the selection.        
        while i <= mid and j < n : 
            if check :
                res.append(nums[j])
                j +=  1 
                check = 0
            else : 
                res.append(nums[i])
                i += 1
                check = 1 
        # any left elements will be added ;)        
        while i <mid : 
            res.append(nums[i])
            i += 1 
                
        return res 