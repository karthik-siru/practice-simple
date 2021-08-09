'''
Print all the subarrays with sum 0  
'''

class Solution:
    #Function to count subarrays with sum equal to 0.
    def findSubArrays(self,arr,n):
        
        # stores the indices of particular sum 
        hash_table = {}
        
        sum =0 
        
        # this is for the subarrays starts from index 0  
        hash_table[0] = [-1]
        res = []
        
        for i in range(len(arr)) :
            sum +=  arr[i]
            
            if sum in hash_table : 
                hash_table[sum].append(i)
            else :
                hash_table[sum] =[]
                hash_table[sum].append(i)
            # iterate over all the indices with sum . 
            for start in hash_table[sum] :
                if start != i :
                    res.append(arr[start+1 :  i +1 ])
                    
        return res
                