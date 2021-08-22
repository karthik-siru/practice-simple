
#approach : 
'''
FROM GEEKS-FOR-GEEKS 

-> This problem can be solved using greedy approach,
If total cost is denoted by S, then S = a1w1 + a2w2 … + akwk,
where wi is a cost of certain edge cutting and ai is corresponding coefficient,
The coefficient ai is determined by the total number of cuts
we have competed using edge wi at the end of the cutting process.
Notice that sum of the coefficients is always constant, 
hence we want to find a distribution of ai obtainable such that S is minimum. 
To do so we perform cuts on highest cost edge as early as possible, 
which will reach to optimal S. If we encounter several edges having the same cost,
we can cut any one of them first. 

'''

class Solution : 
    def minCostCut(self, h, v ): 
        m,n = len(v), len(h)

        h.sort(reverse = True )
        v.sort(reverse = True )

        i, j = 0, 0  
        cost = 0
        h_count , v_count = 1, 1 
        while i <n and j <m : 
            #go with the max_value 
            if h[i] > v[j] : 
                cost += v_count*h[i]
                h_count += 1 
                i += 1 
            else : 
                cost += h_count*v[j]
                v_count += 1 
                j += 1 
        #if vertical cuts completed :
        while i< n : 
            cost += v_count*h[i]
            h_count += 1 
            i += 1 
        #all horixantal cuts completed
        while j <m :
            cost += h_count*v[j]
            v_count += 1 
            j += 1 

        return cost 