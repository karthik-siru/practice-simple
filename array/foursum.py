#approach : 
'''
The idea is to consider every pair of elements in the array one by one 
and insert it into a hash table. 
For each pair of elements (i, j), calculate the remaining sum. 
If the remaining sum exists in the map and elements The idea is to consider every pair of elements in the array one by one and insert it into a hash table. For each pair of elements (i, j), calculate the remaining sum. If the remaining sum exists in the map and elements involved in the previous occurrence doesn’t overlap with the current pair, i.e., (i, j, i, y) or (i, j, x, i) or (i, j, j, y), or (i, j, x, j), print the quadruplet and return.involved in the previous 
occurrence doesn’t overlap with the current pair, 
i.e., (i, j, i, y) or (i, j, x, i) or (i, j, j, y), or (i, j, x, j),
 print the quadruplet and return.
'''

# Function to check if quadruplet exists in a list with the given sum
def hasQuadruplet(A, target):
 
    # create an empty dictionary
    # `key` —> target of a pair in the list
    # `value` —> list storing an index of every pair having that sum
    dict = {}
 
    # consider each element except the last element
    for i in range(len(A) - 1):
 
        # start from the i'th element until the last element
        for j in range(i + 1, len(A)):
 
            # calculate the remaining sum
            val = target - (A[i] + A[j])
 
            # if the remaining sum is found on the dictionary,
            # we have found a quadruplet
            if val in dict:
 
                # check every pair having a sum equal to the remaining sum
                for pair in dict[val]:
                    x, y = pair
 
                    # if quadruplet doesn't overlap, print it and return true
                    if (x != i and x != j) and (y != i and y != j):
                        print("Quadruplet Found", (A[i], A[j], A[x], A[y]))
                        return True
 
            # insert the current pair into the dictionary
            dict.setdefault(A[i] + A[j], []).append((i, j))
 
    # return false if quadruplet doesn't exist
    return False
 
 
if __name__ == '__main__':
 
    A = [2, 7, 4, 0, 9, 5, 1, 3]
    target = 20
 
    if not hasQuadruplet(A, target):
        print("Quadruplet Doesn't Exist")