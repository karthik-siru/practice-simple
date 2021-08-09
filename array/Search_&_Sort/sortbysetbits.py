class Solution:
    
 
    def countBits(self,a):
        count = 0
        while (a):
            if (a & 1 ):
                count += 1
            a = a>>1
        return count
     
    # Function to sort according to bit count
    # This function assumes that there are 32
    # bits in an integer.
    def sortBySetBitCount(self,arr,n):
        count = [[] for i in range(32)]
        setbitcount = 0
        for i in range(n):
            setbitcount = self.countBits(arr[i])
            count[setbitcount].append(arr[i])
     
        j = 0 # Used as an index in final sorted array
     
        # Traverse through all bit counts (Note that we
        # sort array in decreasing order)
        for i in range(31, -1, -1):
            v1 = count[i]
            for i in range(len(v1)):
                arr[j] = v1[i]
                j += 1
