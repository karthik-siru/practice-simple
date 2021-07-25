'''
Min number of knight steps needed to reach the target position 

'''


#aPPROACH :
'''
Same as flood fill  algorithm , we inserted a null to keep track of the levels
count 
'''

from collections import deque

class Solution:
    
    
    # validates , whether a row and col valid or not 
    def validator(self, row , col , N ) :
        if row >N-1  or row <0  or col >N-1 or col < 0 :
            return False
            
        return True 
    
        

	#Function to find out minimum steps Knight needs to reach target position.
    def minStepToReachTarget(self, knightPos, targetPos, N):
		
            dr = [2, 2, -2 , -2 , 1 , 1, -1, -1 ]
            dc = [1 ,-1, 1, -1 , 2, -2, 2 ,-2 ]
            
            visited =[[False for i in range(N+1)] for j in range(N+1)]
            
            visited[knightPos[0]][knightPos[1]] = True 
            
            count =  1  
            null = (-1 , -1 )
            
            q =  deque()
            q.append ((knightPos[0], knightPos[1]))
            q.append(null)
            
            while q : 
                
                (row , col )  = q.popleft()
                
                if row ==-1 and col ==-1 :
                    count +=  1 
                    q.append(null)
                    continue 
                # we will take all the 8 steps possible for knight.
                for i in range(8) :
                    
                    row +=  dr[i]
                    col +=  dc[i] 
                    
                    if self.validator(row, col , N) and not visited[row][col] :

                        if row == targetPos[0] and col == targetPos[1] :
                            return count 
                        
                        q.append((row, col))
                        visited[row][col]  = True 
                        
                    row -=  dr[i]
                    col -=  dc[i]
		            

		    