
'''

# of ways to get sum N =  # of ways to get sum N-1 + 
                          # of ways to get sum N-2 +
                          # .....
                          # of ways to get sum N-6 .

with terminating conditions ::

   1) if n < 0  :
         # of ways = 0
   2) if n == 0 :  ( i.e not taking anything )
         # of ways = 1

   Note that 1+2+2 and 2+1+2 is different .

'''

def  dice(n):
   if n < 0 :
      return 0 
   else :
      dp = [1]
      for i in range(1,n+1):
         res = 0
         if i-1 >= 0:
            res += dp[i-1]
         if i-2 >= 0:
            res += dp[i-2]
         if i-3 >= 0:
            res += dp[i-3]
         if i-4 >= 0:
            res += dp[i-4]
         if i-5 >= 0:
            res += dp[i-5]
         if i-6 >= 0:
            res += dp[i-6]

         dp.append(res)
      return dp[-1]%(10**9 + 7)
         
         



n = int(input())

print(dice(n))
