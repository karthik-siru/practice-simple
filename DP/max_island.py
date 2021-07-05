'''

The idea is simple , whenever you find a land i.e 1 , just look around it to append to this land .    

and the that grid[][] value is made 0 , to not recalculate the island .

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid) , len(grid[0])
        ans = 0
        def sum_land (i ,j ):
            if i < 0  or j < 0 or i >= n or j >= m or grid[i][j] == 0:
                return 0 
            grid[i][j] = 0
            return 1 + sum_land(i-1 , j) + sum_land (i, j-1) + sum_land(i , j+1) + sum_land(i+1 , j)
        
        for i in range (n) :
            for j in range(m) :
                if grid[i][j] :
                     ans = max(ans , sum_land(i, j))
        return ans 
