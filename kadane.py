l = [int(i) for i in input().split(" ")]

# Kadane's algorithm 

max_sum_ending_here , max_sum_sofar =  0, 0

for i in l :
    max_sum_ending_here +=  i 

    if max_sum_ending_here < 0 :
        start =  l.index(i)
        max_sum_ending_here = 0
    
    if max_sum_sofar < max_sum_ending_here :
        max_sum_sofar = max_sum_ending_here
        end =  l.index(i) 

print(start+1 , end , max_sum_sofar)
