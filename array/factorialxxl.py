#question : 
'''
return the factorial of large numbers.( I mean which are greater than 2^64 bit numbers)

'''

#approach : 
'''
->  GO back to school and learn multplication 
->  Coz ... we will use that technique ;)
'''


class Solution:
    def factorial(self, n):
        #code here
        
        if n <2 : 
            return [1]
        
        fact = [1]
        i = 2 
        while i <= n  : 
            carry =  0  
            for j in range(len(fact)-1 , -1, -1): 
                num = i*fact[j] + carry 
                carry = num//10
                fact[j] = num%10 
            if carry : 
                fact.insert(0 , carry)
                
            i +=  1 
            
        return fact 
            