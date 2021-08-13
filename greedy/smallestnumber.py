#question : 
'''
Given the sum and number of digits in a number . Return the smallest number possible 
with such  combinations .  
'''

#Approach ; 
'''
We initially deduct 1 from sum s so that we have smallest digit at the end. 
After deducting 1, we apply greedy approach. 
We compare remaining sum with 9, if remaining sum is more than 9,
we put 9 at the current position, else we put the remaining sum.
Since we fill digits from right to left, we put the highest digits on the right side.
'''

# Key point : 
'''
The only tricky thing of above algo. is that why s need to deduct by one.

Let sum of digits as s, number of digits be d.
When s is positive multiple of d, which means s = kd, (k >= 1).
We may yield a strange lengthed d number.

Consider s = 18, d = 3, which 18 = 6 * 3.
If we don't deduct s by one beforehand, we yield a result of
{0, 9, 9}, which is 099. But the preceding zero is doesn't count.

So it's why it need to deduct by one.

And you can find that res[0] = s + 1; yields a range of [1, 9]
Which assure that the most significant digit is not zero.
'''


class Solution : 

    def smallestNumber (self, s ,n) :
        # only possible solution 
        if s == 0: 
            if n == 1:
                return  0 
            else : 
                return -1 
        # no solution 
        if s >9*n : 
            return -1 

        res  = [0 for i in range(n)]
        s -= 1
        for i in range(n-1,0,-1):
            if s >9 : 
                res[i] = 9
                s -= 9 
            else : 
                res[i] = s 
                s = 0

        res[0] = s+1
        
        result = 0
        
        for i in  res : 
            result *= 10
            result += i
            
        return result 

        