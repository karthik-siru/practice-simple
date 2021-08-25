def pageFaults( N, C, pages):
    # code here
    
    lr = 0
    active =  set()
    count = 0
    
    for i in range(N): 
        if pages[i] in active :
            pass 
        elif i < C or len(active) < C :
            active.add(pages[i])
            count += 1 
        else :
            active.remove(pages[lr])
            active.add(pages[i])
            lr += 1 
            count +=1
        print(count , active )

a = [5, 5, 1, 3, 2, 4, 1, 0, 5]
N = 9 
C = 4 

pageFaults(N,C,a)