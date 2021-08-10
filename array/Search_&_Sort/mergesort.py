# Inplace Merge Sort : 
'''

Maintain two pointers that point to the start of the segments which have to be merged.
Compare the elements at which the pointers are present.
If element1 < element2 then element1 is at right position, simply increase pointer1.
Else shift all the elements between element1 and element2(including element1 but excluding element2) right by 1
and then place the element2 in the previous place(i.e. before shifting right) of element1. 
Increment all the pointers by 1.

'''


class Solution : 

    def merge (self,nums, start , mid , end) : 
        start2 = mid + 1

        if nums[mid] < nums[start2] : 
            return 
        
        while start <= mid and start2 <= end : 
            if nums[start] < nums[start2] : 
                start += 1 
            else : 
                value =  nums[start2]
                index =  start2
                
                while index > start: 
                    nums[index] =nums[index-1]
                    index -= 1 

                nums[start] = value 
                start += 1 
                mid +=  1 
                start2 += 1 

    def mergeSort(self, nums , start , end ) : 
        if start <  end : 
           mid  = (start +  end)//2 
           self.mergeSort(nums , start , mid-1 )
           self.mergeSort(nums , mid +1 , end )
           self.merge(nums , start , mid , end )

        
