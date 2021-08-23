#question : 
'''
Given an array a[ ] of N elements.
Consider array as a circular array i.e. element after an is a1. 
The task is to find maximum sum of the absolute difference between 
consecutive elements with rearrangement of array elements allowed i.e. 
after any rearrangement of array elements find |a1 – a2| + |a2 – a3|
 + …… + |an-1 – an| + |an – a1|.
'''

#approach : 
'''
->  So .. let's assume the numbers are  a , b ,c , d ,e .. in  sorted order.  

->  So ,we get  the max .. dif by this arrangement -->   a,e,b,d,c  
->  Hence the diff would be -->  (e-a) + (e-b) + (d-b) + (d-c) + (c-a)
->  i.e ---.. 2*e + 2*d  - 2*a -2*b 

->  So we can simply subtract numbers upto mid and add after mid .
'''

def maxSum(arr,n):
    # code here
    #sort the array 
    arr.sort()
    sum = 0
    # loop upto mid-val 
    for i in range(len(arr)//2):
        sum -= (2 * arr[i])
        sum += (2 * arr[n - i - 1])
        
    return sum 
        
