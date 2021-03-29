
test = int(input())

while  test  :

    n , m  = ( int(i)  for i in input().split(' '))

    if n > m :
       if  n%2 == 1 :
          print( (n-1)**2 + m )
       else :
          print ( n**2 - m + 1 )
       
    else :
       if m %2 == 1 :
          print ( m**2 - n + 1 )
       else :
          print ( (m-1)**2 + n )
          
    test -= 1 
