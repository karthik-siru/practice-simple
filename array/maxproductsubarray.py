#question : 
'''
maximum product sunnset of an array .  
'''

#approach : 
'''
->  even no. of  negative numbers  ----> product of all except zeros 
->  odd no.of negative numbers     ----> product of all numbers .. except the zeros 
                                         and -ve nnumber with least abs value 
->  All zeros and one negative  --->  0
'''

def maxProductSubset(a, n):
    if n == 1:
        return a[0]
    max_neg = -999999999999
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(n):
 
        # If number is 0, we don't
        # multiply it with product.
        if a[i] == 0:
            count_zero += 1
            continue
        #count -ve s and min abs value 
        if a[i] < 0:
            count_neg += 1
            max_neg = max(max_neg, a[i])
 
        prod = prod * a[i]
 
    # If there are all zeros
    if count_zero == n:
        return 0
 
    # If there are odd number of
    # negative numbers
    if count_neg & 1:
 
        # Exceptional case: There is only
        # negative and all other are zeros
        if (count_neg == 1 and count_zero > 0 and
            count_zero + count_neg == n):
            return 0
        # divide the product by least abs value
        prod = int(prod / max_neg)
 
    return prod