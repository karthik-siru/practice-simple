class Solution:
	def setBits(self, N):
		# code here
		
		count = 0  
		
		while N :
		    count +=1 
		    N &= (N-1)
		    
		return count 