
'''
Given a binary tree root, find the most frequent subtree sum. 
The subtree sum of a node is the sum of all values under a node, including the node itself. You can assume there is one unique solution.

Constraints

     n ≤ 100,000 where n is the number of nodes in root
     
     
Input :

[ node.val , [left subtree ] , [right subtree ] ] 

root = [5, [2, null, null], [-5, null, null]]

Output
2
Explanation
2 occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
     
     
'''



# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        maxi = {} # this dictionary contains various sums encountered during the traversal 

        def sum_count (self , root , maxi ):

            if not root :   # base case 
                return 0 
            
            ls,rs = sum_count(self , root.left , maxi) , sum_count (self , root.right , maxi)
            
            key = ls + rs +root.val
            
            if key not in maxi : # if it is not in the dictionary , add it 
                maxi[key] = 1
            else :               # else , add 1 to it . 
                maxi[key] += 1

            return key  # return the sum . 

        sum_count(self , root , maxi )

        return max(maxi , key = maxi.get)
