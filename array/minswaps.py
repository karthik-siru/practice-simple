#question : 
'''
Given an array .. return min number of swaps required to make the array sorted 
'''

#approach : 
'''
->  maintain an dictionary . which stores indices of elements in gven array
->  dictionary is to get numbers quickly.
->  make  a sorted array with given elements 
->  Now maintain two poiinters i , and j .. which points to nums and sortednums
->  Start both of them from the end .. 
->  If both are same .. then decrement both 
(n1 ->  number pointed by i and  n2 -> number pointed by j )
->  else .. swap the n1 in nums .. with n2 in nums 
->  also update the index of the swapped elements .
->  decrement i and j  and maintain a count for the final answer.
'''

#Note :
# you can start froom the front and update also ;)

class Solution:   
    #Function to find the minimum number of swaps required to sort the array.
	  def minSwaps(self, nums):
            #maintain a dictionary 
            index = {}
            n =  len(nums)  
            # store the indices.
            for i in range(n):
                index[nums[i]] =  i 
                
            sortednums = sorted(nums)
            #iterators for nums and sortednums
            i, j = n-1 , n-1 
            count = 0
            
            while j >0 : 
                # if both are not equal 
                #swap and update the index 
                if sortednums[j] != nums[i] : 
                    a = index[sortednums[j]]
                    index[nums[i]] = a 
                    nums[a], nums[i] = nums[i] , nums[a]
                    count += 1 
                i -=  1 
                j -=  1 
                    
            return count 