
'''

start from top-right corner .. is the biggest hint ;)


'''



def solve(self, a, target):
        n ,m  =  len(a) , len(a[0])
        i, j  = 0 , m-1 

        while i < n  and j >= 0:
                if a[i][j] ==  target  :
                    return True 
                elif a[i][j] < target : 
                    i+= 1
                else :
                    j -= 1 
        
        return False 
