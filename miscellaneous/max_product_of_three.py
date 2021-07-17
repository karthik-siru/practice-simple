'''
Idea :
  
   just think after sorting the numbers lists , which numbers will you 
   take to make  maximum product . 

   ->  option1  -> two negative and one positive 
   ->  option2  -> three positive 

   think for option one and option two ;) 

'''

class Solution:
    def solve(self, nums):
        nums.sort()

        negative_product = nums[0] *nums[1]*nums[-1]

        positive_product = nums[-1]*nums[-2]*nums[-3]

        return max(negative_product, positive_product )