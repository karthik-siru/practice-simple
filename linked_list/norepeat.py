#approach : 
'''
->  maintain a hash_map and a queue .. every time .. append 1 to it's count
    in hash_map and append it into a queue.
->  if the first entry in q has a count>1 .. pop it otherwise .. add it to the
    resultant string . 
->  If the queue is empty ... append "#"
'''

class Solution:
	def FirstNonRepeating(self, s):
		# Code here
		
		if len(s) <  2 : 
		    return s 
		    
		q = []
		
		hash_map  = {}
		
		res = ""
		
		for i in s : 
		    hash_map[i] = hash_map.get(i, 0) + 1 
		    
		    q.append(i)
		    
		    while q : 
		        
		        if hash_map[q[0]] > 1 : 
		            q.pop(0)
		        else : 
		            break 
		        
		    if not q : 
		        res += "#"
		    else : 
		        res += q[0]
		        
		return res 
		            