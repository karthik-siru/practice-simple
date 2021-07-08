
'''
Algorithm : 

      Search for the element from the end , such that it's preceding element is 
      greater than itself. 
      
      if you can't find any such element , then the number is already at it's max value.

      let it's index be i .

      from there to right of the ith element , search for  smallest element  which is greater 
      than the ith element and swap them .

      Now , reverse the right side part of the ith element . ;)



'''


class Solution:
    def nextPermutation(self, N, nums):
        # code here
        
        for i in range(N-1,-1,-1):        
            if nums[i-1]<nums[i]:
                break
        if i!=0 :
            for j in range(N-1,-1,-1):
                if nums[j]>nums[i-1]:
                    break 
            nums[i-1],nums[j]= nums[j],nums[i-1]
        nums[i:]=reversed(nums[i:])
        
        return nums
        