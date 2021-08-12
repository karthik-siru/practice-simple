#Question : 
'''
A little girl darla counts from 1 to 1000 using the fingers of her left hand as
follows. She starts by calling her thumb 1, the first finger 2, middle finger 3,
ring finger 4, and little finger 5. Then she reverses direction, calling the ring
finger 6, middle finger 7, the first finger 8, and her thumb 9, after which she
calls her first finger 10, and so on. If she continues to count in this manner,
on which finger will she stop?
'''

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

