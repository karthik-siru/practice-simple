'''

Idea : 
-> If egg breaks at ith floor , then our problem reduced to (Floors-1 , Eggs-1)
-> else our problem reduced to (Floors -i , Eggs )

'''

class Solution:
    
    def eggDrop(self,n, k):
        # code here
        
            eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]
         
            # Base cases 
            # ->  1 floor and n eggs =  1 
            # ->  0 floors and n eggs = 1
            for i in range(1, n + 1):
                eggFloor[i][1] = 1
                eggFloor[i][0] = 0
         
            # -> n floors and 1 egg ->  n
            for j in range(1, k + 1):
                eggFloor[1][j] = j
         
            #  i ->  eggs 
            #  j -> floors 
            for i in range(2, n + 1):
                for j in range(2, k + 1):
                    eggFloor[i][j] = 99999999
                    for x in range(1, j + 1):
                        res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x])
                        if res < eggFloor[i][j]:
                            eggFloor[i][j] = res
        
            return eggFloor[n][k]