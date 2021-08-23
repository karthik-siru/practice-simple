
#approach : 
'''
->  Start from the first chick from the barn and see .. whether it can cross the 
    barn or not 
->  IF not_possible swap with the faster-chick .
'''
class Solution : 

    def pickChicks(self, x,v,k,t, b):

        n =  len(x)
        swaps , not_possible = 0, 0 
        count = 0
        for i in range(n-1, -1, -1 ) : 
            distance_needed = b-x[i]
            distance_possible = v[i]*t


            if distance_possible >= distance_needed :
                count += 1 
                if not_possible >=0 : 
                    swaps += not_possible
            else : 
                not_possible += 1 

            if count>=k : 
                return True 

        return count>=k 


            