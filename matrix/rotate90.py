#question  
'''
->  Given a matrix .. return the 90 deg clockwise rotation of the matrix 
'''

#approach : 
'''
->  The most simple approach is that 1)Reverse the matrix row-wise 
->  2) Transpose the matrix .
->  So simple right ;) 

'''

from transpose import Solution

a =  Solution()

def Rotate(matrix):
    matrix = matrix[::-1]
    a =  Solution()

    return a.transpose(matrix)

if __name__ == "__main__" :
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    print(Rotate(a))