# question : 
'''
Given an array A[] of size N and a positive integer K, 
find the first negative integer for each and every window(contiguous subarray) 
of size K.

-> if no such element present print 0 .
'''


#approach : 
'''
->  Store the indices of the negative numbers in the given array  in a 'QUEUE'.
->  iterate from 0 to n-k 
->  Whenever the iterator becomes greater than queue's element --> pop from the queue
->  else if .. queue is empty just add 0 to the result.
->  else .. get the index  from top  of the queue 
->  if that index is within the bounds of the window ... add it to result else 
    add 0 .
'''

def printFirstNegativeInteger( A,n,k):
    # code here\
    
    res = []
    q = []
    # store indices 
    for i in range(n) :
        if A[i] < 0:
            q.append(i)
    
    for i in range(n-k+1) : 
        # set the valid queue top
        while q and i >  q[0] : 
            q.pop(0)
        # no queue just add 0     
        if q == []: 
            res.append(0)
            continue     
        # get index from queue
        index = q[0]
        # if valid index add it 
        if i<= index < i + k : 
            res.append(A[index])
        else : 
            res.append(0)
                   
    return  res 