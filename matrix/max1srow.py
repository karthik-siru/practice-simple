# question :
'''
->  Return the index of  max number of 1's in a row .
'''

#approach : 
'''
->  Start from the top-right-corner .. now 
->  If we encounter a 1 move left otherwise move down 
->  Keep track of the max_row_index till now ..  
'''

class Solution:
    def rowWithMax1s(self, arr, n, m):
        r = 0
        c = m-1
        max_row_index=-1

        while r<n and c>=0 :
            # move left 
            if arr[r][c] == 1:
                max_row_index = r
                c-=1
            # move down 
            else :
                r+=1
        
        return max_row_index