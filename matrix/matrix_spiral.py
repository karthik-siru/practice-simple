'''

Given the matrix , eturn the list of  spiral traversal of the matrix .. 

example :
   
   matrix = [
    [6, 9, 8],
    [1, 8, 0],
    [5, 1, 2],
    [8, 0, 3],
    [1, 6, 4],
    [8, 8, 10]
]


output ::
  
  [6, 9, 8, 0, 2, 3, 4, 10, 8, 8, 1, 8, 5, 1, 8, 1, 0, 6]


using four  pointers and dire ction variable .. to travel 


'''




class Solution:
    # using four pointers method
    def solve(self, matrix):
        if not matrix :
            return []
        top , left = 0, 0 
        down , right = len(matrix)-1 , len(matrix[0])-1
        dirc  = 0 #which direction to go .. 0 -> right , 1-> down , 2-> left , 3 ->top 
        l = []
        while top <= down and left <= right :
            if dirc == 0:
                for i in range (left , right+1 ):
                    l.append(matrix[top][i])
                top += 1
                dirc = 1
            elif dirc == 1 :
                for i in range(top , down+1 ):
                    l.append(matrix[i][right])
                right -= 1
                dirc = 2 
            elif dirc == 2 :
                for i in range (right , left-1 , -1 ):
                    l.append(matrix[down][i])
                down -= 1
                dirc = 3
            else :
                for i in range(down , top-1 , -1) :
                    l.append(matrix[i][left])
                left += 1
                dirc = 0 
        return l 
