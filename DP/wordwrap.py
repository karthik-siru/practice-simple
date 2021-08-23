class Solution:
	def solveWordWrap(self, nums, k):
		#Code here

            inf = 999999999
            n =  len(nums)
            
            cost = [[0 for i in range(n)] for j in range(n)]
            
            for i in range(n) : 
                cost[i][i] = k - (nums[i])
                for j in range(i+1, n ) : 
                    cost[i][j] = cost[i][j-1] - (nums[j]) -1
                    
                    
            for i in range(n) :
                for j in range(i, n):
                    if cost[i][j] < 0 : 
                        cost[i][j] = inf 
                    else : 
                        cost[i][j] =  cost[i][j]**2 
            
            minCost = [0  for i in range(n)]            
                        
            for i in range(n-1, -1, -1 ) : 
                minCost[i] = cost[i][n-1]
                for j in range(n-1 , i, -1 ) : 
                    if cost[i][j-1] == inf : 
                        continue 
                    a = minCost[j] + cost[i][j-1]
                    
                    minCost[i] = min(minCost[i] , a )
                    
                return minCost[0]