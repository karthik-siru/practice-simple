
from collections import deque

class Solution:
    
    #   USING BFS STRATEGY : 

    def floodFill(self, image, sr: int, sc: int, newColor: int):
        oldColor =  image[sr][sc]
        q =  deque()
        
        q.append((sr, sc))
        
        while q :
            (row ,col) = q.popleft()
            
            if row <0 or row >= len(image)  or col < 0 or col >= len(image[0]):
                continue 
            if image[row][col]  == newColor :
                continue 
            if image[row][col]  == oldColor  :
                image[row][col]  = newColor 
                
                q.append((row-1 , col))
                q.append((row+ 1, col))
                q.append((row, col-1))
                q.append((row , col +1 ))
                
        return image 


    # USING DFS STRATEGY :

    def floodFilldfs(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image