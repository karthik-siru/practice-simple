'''
   
   Time ->  O(n**2) : 

       Let's create an array ,which stores the LIS upto A[0..i] , which 
       includes A[i] 

       Now , max of the LIS array will be our answer .


   Time ->  O(n*logn): 

       -we maintain some active lists : 

       Case1 ->  No  active lists create one
       Case2 ->  when you found a number greater than active lists last element 
                 clone the active list and append the element founded 
       Case3 ->  When after extending , len becomes a known value discard it .

Note : At any instance during our construction of active lists, the following condition is maintained.
“end element of smaller list is smaller than end elements of larger lists”.

Example  A =[0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

        A[0] = 0. Case 1. There are no active lists, create one.
        0.
        -----------------------------------------------------------------------------
        A[1] = 8. Case 2. Clone and extend.
        0.
        0, 8.
        -----------------------------------------------------------------------------
        A[2] = 4. Case 3. Clone, extend and discard.
        0.
        0, 4.
        0, 8. Discarded
        -----------------------------------------------------------------------------
        A[3] = 12. Case 2. Clone and extend.
        0.
        0, 4.
        0, 4, 12.
        -----------------------------------------------------------------------------
        A[4] = 2. Case 3. Clone, extend and discard.
        0.
        0, 2.
        0, 4. Discarded.
        0, 4, 12.
        -----------------------------------------------------------------------------
        A[5] = 10. Case 3. Clone, extend and discard.
        0.
        0, 2.
        0, 2, 10.
        0, 4, 12. Discarded.
        -----------------------------------------------------------------------------
        A[6] = 6. Case 3. Clone, extend and discard.
        0.
        0, 2.
        0, 2, 6.
        0, 2, 10. Discarded.
        -----------------------------------------------------------------------------
        A[7] = 14. Case 2. Clone and extend.
        0.
        0, 2.
        0, 2, 6.
        0, 2, 6, 14.
        -----------------------------------------------------------------------------
        A[8] = 1. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 2. Discarded.
        0, 2, 6.
        0, 2, 6, 14.
        -----------------------------------------------------------------------------
        A[9] = 9. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 2, 6.
        0, 2, 6, 9.
        0, 2, 6, 14. Discarded.
        -----------------------------------------------------------------------------
        A[10] = 5. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 1, 5.
        0, 2, 6. Discarded.
        0, 2, 6, 9.
        -----------------------------------------------------------------------------
        A[11] = 13. Case 2. Clone and extend.
        0.
        0, 1.
        0, 1, 5.
        0, 2, 6, 9.
        0, 2, 6, 9, 13.
        -----------------------------------------------------------------------------
        A[12] = 3. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 1, 3.
        0, 1, 5. Discarded.
        0, 2, 6, 9.
        0, 2, 6, 9, 13.
        -----------------------------------------------------------------------------
        A[13] = 11. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 1, 3.
        0, 2, 6, 9.
        0, 2, 6, 9, 11.
        0, 2, 6, 9, 13. Discarded.
        -----------------------------------------------------------------------------
        A[14] = 7. Case 3. Clone, extend and discard.
        0.
        0, 1.
        0, 1, 3.
        0, 1, 3, 7.
        0, 2, 6, 9. Discarded.
        0, 2, 6, 9, 11.
        ----------------------------------------------------------------------------
        A[15] = 15. Case 2. Clone and extend.
        0.
        0, 1.
        0, 1, 3.
        0, 1, 3, 7.
        0, 2, 6, 9, 11.
        0, 2, 6, 9, 11, 15. <-- LIS List
        --------------------------------------------------------------------------

        '''    
    

class Solution :

    #method 1 
    def longestSubsequence(self,a,n): 
        lis = [1]*n 
        
        for i in range (n) :
            for j in range(i):
                if a[j] < a[i] :
                    lis[i] =  max(lis[i] , lis[j]+1)
                    
        return max(lis)

    #method 2 

    def CeilIndex(self,A, l, r, key):
 
        while (r - l > 1):
         
            m = l + (r - l)//2
            if (A[m] >= key):
                r = m
            else:
                l = m
        return r
    
    def LongestIncreasingSubsequenceLength(self, A, size):
           
        tailTable = [0 for i in range(size + 1)]
        len = 0 # always points empty slot
      
        tailTable[0] = A[0]
        len = 1
        for i in range(1, size):
         
            if (A[i] < tailTable[0]):
     
                # new smallest value
                tailTable[0] = A[i]
      
            elif (A[i] > tailTable[len-1]):
     
                # A[i] wants to extend
                # largest subsequence
                tailTable[len] = A[i]
                len+= 1
      
            else:
                # A[i] wants to be current
                # end candidate of an existing
                # subsequence. It will replace
                # ceil value in tailTable
                tailTable[self.CeilIndex(tailTable, -1, len-1, A[i])] = A[i]
                
        return len
