'''
 Given an sorted array, check whether there exits an index where nums[index] == index 
 if exits , return the smallest index , else return -1 . 
'''

#Approach : 
'''
  We use binary search , to decide which way to go , either to left  or right .
'''

class Solution:
    def solve(self, nums):
        inf = 99999999

        l , r = 0 , len(nums)-1 
        minimum =  inf 
        while l <= r : 
            mid =  (l+r)//2
            if nums[mid] == mid :
                minimum =  min(mid , minimum)
                r =  mid -1 
            elif nums[mid] >  mid : 
                r = mid -1 
            else : 
                l =  mid + 1 

        return -1 if minimum == inf else minimum 