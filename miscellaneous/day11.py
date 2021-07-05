'''
   
    ok , let's see the logic , every number can be expressed in the form of  9x or 9x+k    
    
    1) sum of numbers divisible by 9 is 9 . 
       
        ex : 81  ---------  8+1 = 9 
             45  ---------  4+5 = 9 
 
'''



def Sum_untill_single_digit( n ) :
  
  if  n == 0 :
     return 0 
    
  elif  n%9== 0 :
     return 9
  else :
     return n%9
