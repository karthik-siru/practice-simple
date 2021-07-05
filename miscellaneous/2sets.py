
n = int(input())

if (n%2 == 1 and (n-3)%4 !=0 )  or (n%2 == 0 and (n-4)%4 !=0 ) :
   print ("NO")

else :
   print ("YES")
   if n%2 == 1:   
     print ((n+1)//2)
     print ("1 2" , end = " " )
     i = 4
     while i <= n :
        print (i,end = " ")
        if i%2 ==1 :
           i+=1
        else :
           i+=3 
     print ("")
     print ((n-1)//2)
     print ("3", end = " ")
     i = 5
     while i <= n :
         print (i , end = " ")
         if i%2 == 0:
            i+=2 
         else :
            i+=1 
     print ("")  
     
     
   else :
     i = 1
     print (n//2)
     while i <= n :
        print(i ,end = " ")
        if i%2 == 0 :
           i+=1 
        else :
           i+=3
     print ("")
     print(n//2)
     i = 2
     while i<= n :
        print (i,end = " ")
        if i %2 == 0:
           i+= 1
        else :
           i+=2 
