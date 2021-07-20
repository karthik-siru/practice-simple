#Question : 

'''
So , there is an array of numbers , find the maximum 
sum subsequence found , such that you cannot select 
1) 2 contiginous elements 
2) 3 contiginous elements 

'''

#Idea : 

'''
SO , for each element we have two possibilities 
to include it or to exclude it .

->  M(i) -> max sum possible with upto ith index  elements

->  Suppose we know M(i-1) and M(i-2)


                 
M(i) =  max ( 
                A(i) + M(i-2), #include 
                M(i-1), #exclude 
            )

similarly for 3 cont.. 

M(i)  =  max (   
                 A(i) + A(i-1) + M(i-3), 
                 A(i) +M(i-2)
                 M(i-1)
             )
           

'''

class Solution : 

    def non2Contiginous(self, a):
        n =  len(a)
        dp = [0 for i in range(n)] 
        dp[0] = a[0]
        dp[1] = max(a[0], a[1] )
        
        for i in range(2, n) :
            dp[i] = max(a[i-1] + dp[i-2] , dp[i-1])

        return dp[-1]

    def non3Contiginous(self, a):
        n =  len(a)
        dp = [0 for i in range(n)]

        dp[0]  = a[0]
        dp[1]  = max(a[1] , a[1]+a[0] , a[0])
        dp[2]  = max(dp[1], dp[0]+a[2] , a[1] + a[2])

        for i in range(3,n) :
            dp[i]  = max(
                           a[i]+a[i-1]+dp[i-3],
                           dp[i-2] +a[i],
                           dp[i-1]
                        ) 

        return dp[-1]