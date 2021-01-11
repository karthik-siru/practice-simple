def reverseLookup(dictionary , val) :
    l = []
    
    for i,j in dictionary.items() :
       if  j == value :
          l.append(i)
          
    return l


n = int (input('enter the number of key- value pairs'))

dic = {}

for i in range (0,n):
     s = input()
     v = input()
     
     dic[s] = v 

value = input ()


l = reverseLookup(dic, value)

print (l)     
