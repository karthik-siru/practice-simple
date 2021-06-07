'''

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:        
        a = 0
        b= 0
        for i in range(2, len(cost) + 1):
            temp = a
            a = min(a + cost[i - 1], b + cost[i - 2])
            b = temp

        return a
