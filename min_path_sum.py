'''

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

'''


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n , m  = len(grid) , len(grid[0])
        l = [[0 for i in range(m)] for j in range(n)]
        l[0][0] =  grid[0][0] 

        # initialise thedp array

        for i in range(1, m ):
            l[0][i] = l[0][i-1] + grid[0][i]
        for i in range (1, n):
            l[i][0] = l[i-1][0] + grid[i][0]

        # calculate the remaining dp matrix 

        for i in range(1,n):
            for j in range(1,m):
                l[i][j] = min(l[i-1][j] , l[i][j-1]) + grid[i][j]
        return l[n-1][m-1]
