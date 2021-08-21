class Solution : 
    def copybits(self, x, y, l, r ) :
        power = 2**(r-l +1) - 1 
        mask =  power<<(l-1)
        return (x)|(y&mask)

x,y = [int(i)  for i in input().split()]
l,r = [int(i)  for i in input().split()]

a =  Solution() 

print(a.copybits(x,y,l,r))