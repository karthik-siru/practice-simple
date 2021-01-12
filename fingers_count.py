def is_even( n ):
  return ((int (n/4) % 2 ) == 0)
  
print('Hey! my friend darla will tell you the finger of count ')
print('say a number to her ::  starting from 1 ')

n = int(input())

fingers = ['THUMB' , 'INDEX' , 'MIDDLE' , 'RING' , 'LITTLE']

rem =  (n-5)%4 

if ( n-5 ) <=0 :
   print(fingers[n-1],'finger')

else :
   if (is_even(n-5) == 1) :
       print (fingers[-rem -1] ,'finger')
   else :
       print(fingers[rem-1], 'finger')

