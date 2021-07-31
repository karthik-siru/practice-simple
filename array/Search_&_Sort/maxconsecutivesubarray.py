
class Solution : 

    def isConsecutive(self,A, i, j, min, max):
 
        # for a list to contain consecutive integers, the difference
        # between the maximum and minimum element in it should be exactly `j-i`
        if max - min != j - i:
            return False
    
        # create a visited list (we can also use a set)
        visited = [False] * (j - i + 1)
    
        # traverse the sublist and check if each element appears
        # only once
        for k in range(i, j + 1):
    
            # if the element is seen before, return false
            if visited[A[k] - min]:
                return False
    
            # mark the element as seen
            visited[A[k] - min] = True
    
        # we reach here when all elements in the list are distinct
        return True
 
 
    # Find the largest sublist formed by consecutive integers
    def findMaxSublist(self,A):
    
        length = 1
        start = end = 0
    
        # consider each sublist formed by `A[i…j]`
    
        # `i` denotes the beginning of the sublist
        for i in range(len(A) - 1):
    
            # stores the minimum and maximum element formed by `A[i…j]`
            min_val = A[i]
            max_val = A[i]
    
            # `j` denotes the end of the sublist
            for j in range(i + 1, len(A)):
                # update the minimum and maximum elements of the sublist
                min_val = min(min_val, A[j])
                max_val = max(max_val, A[j])
    
                # check if `A[i…j]`is formed by consecutive integers
                if self.isConsecutive(A, i, j, min_val, max_val):
                    if length < max_val - min_val + 1:
                        length = max_val - min_val + 1
                        start = i
                        end = j

            return length 

