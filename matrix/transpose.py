# question : 
'''
->  Given a matrix .. return the transpose without using extra space 
'''


class Solution : 

    def transpose (self, matrix ):
        n =  len(matrix)
        for i in range(n):
            for j in range(i+1, n) : 
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

        return matrix 

if __name__ == "__main__" :
    a = [[1,2,3],
         [4,5,6],
         [7,8,9]]

    t = Solution()
    a = t.transpose(a)


    print(a)
