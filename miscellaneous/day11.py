#question : 
'''
We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?

// start with 49
4 + 9 = 13

// move onto 13
1 + 3 = 4
We would then return 4.
'''


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
