#question : 
'''
Given a string with repeated characters .. rearrange the string such that ..
no adjacent are same 
->  IF not possible print 0 
->  else print 1 
'''

#approach : 
'''
-> Remember majority element .. we will use that here .
-> if there a majority char .. then how bad we arrange letters ..we can't 
   satisfy the given condition .
-> We use this fact to solve this problem. 
'''

class Solution : 

    def rearrange(s) : 
        n =  len(s) 
        
        count = 0  
        char = s[0]
        
        n =  len(s)
        
        for i in range(n) : 
            if count == 0: 
                char = s[i]
                count = 1 
            elif s[i] == char : 
                count += 1
            else : 
                count -=1 
                
        if s.count(char) > n//2 + n%2 :
            print(0)
        else : 
            print(1)

if __name__ == "__main__" :
    t = int(input())
    for i in range(t) : 
        s =  input()
        Solution.rearrange(s)