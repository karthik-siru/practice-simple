# question :
"""
A celebrity is a person who is known to all but does not know anyone at a party. 
If you go to a party of N people, find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that if an 
element of row i and column j  is set to 1 it means ith person knows jth person. 
Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
"""

# approach :
"""
->  Let's  decide the celebrity with the help of row sum .. 
->  Row_sum of celeb is 0 , and col_sum would be n-1 
->  Let's first calculate the row_sum and make a note of the rows, whose sum is 0.
->  Now in the  possible values for rows , let's check their col_sum and decide the 
    celebrity.
"""


class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        row_sum = [0 for i in range(n)]
        # possible values of celebs
        possible = []

        for i in range(n):
            row_sum[i] = sum(M[i])
            if row_sum[i] == 0:
                possible.append(i)
        # no celeb found , we return -1
        celeb = -1

        for col in possible:
            a_sum = 0
            for row in range(n):
                a_sum += M[row][col]
            # found the celeb
            if a_sum == n - 1:
                celeb = col
                break

        return celeb
