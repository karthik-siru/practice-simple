#Boyer–Moore majority vote algorithm :
'''
 ->  MAJORITY-ELEMENT : element which occurs.. more than n//2 times in the array.
 ->  MAINTAIN A ELEMENT m AND  ITERATOR i 
 ->  for i in the nums.length : 
        # if i == 0 : 
              m = nums[i]
              i = 1 
          elif nums[i] == m : 
              i += 1
          else : 
              i -=  1 

 -> FINALLY ,WE WILL BE HAVING  MAJORITY ELEMENT IN m .  
'''


# EXTENDING IT TO N//3 (MAJORITY ELEMENT ) : 

# -->  Similarly  we can extend it to any n//k maority element 

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:       
        # a list of majority elements
        majority = []        
        # threshold for majority validation and verification
        threshold = len(nums) // 3       
        # Record for possible majority candidates, at most two majority elements is allowed by math-proof.
        candidate = [0, 0]   
        # Voting for majority candidates
        voting = [0, 0]  
        ## Step_#1:
        # Find possible majority candidates
        for number in nums:            
            if number == candidate[0]:
                # up vote to first candidate
                voting[0] += 1               
            elif number == candidate[1]:
                # up vote to second candidate
                voting[1] += 1           
            elif not voting[0]:
                # set first candidate
                candidate[0] = number
                voting[0] = 1               
            elif not voting[1]:
                # set second candidate
                candidate[1] = number
                voting[1] = 1               
            else:
                # down vote if mis-match
                voting[0] -= 1
                voting[1] -= 1
           
        ## Step_#2:
        # Validation:
        voting = [0, 0]
        
        for number in nums:
            
            if number == candidate[0]:
                # update up vote for first candidate
                voting[0] += 1
                
            elif number == candidate[1]:
                # update up vote for second candidate
                voting[1] += 1
        
        
        for i, vote in enumerate(voting):            
            # Verify majority by threshold
            if vote > threshold:
                majority.append( candidate[i] )
                       
        return majority
