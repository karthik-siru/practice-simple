'''
Algorithm : 
    It is used in kmp  algorithm , for pattern matching . We maintain two pointers 

    l  = 0  , i = 1    
    
    we traverse through the array :
          
          if we found a match  :
               lps[i] =   l+  1
               increment  l and  i  
          else :
               if we  already found some portion is same , i.e ( l !=  0 )  :
                    move it to the previously matched portion 
                    (matched portion length will be in lps[l -1 ])

              else :
                    lps[i] = 0 
                    increment i  
 '''


class Solution:
       
	def lps(self, s):
        
		# code here
		lps =  [0]*len(s)
		
		i , l =  1, 0  
		
		while i <  len(s)  :
		    
		    if s[i] ==  s[l] :
		        lps[i] =  l + 1 
		        l +=  1
		        i +=  1
		    else :
		        if l != 0 :
		            l =  lps[l-1]
		        else :
		            lps[i] = 0 
		            i +=  1
		return lps
