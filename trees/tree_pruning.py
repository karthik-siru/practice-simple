'''
Given a binary tree root, prune the tree so that subtrees containing all 0s are removed.

Constraints

n ≤ 100,000 where n is the number of nodes in root

Input
root = [0, [1, null, null], [0, [1, [0, null, null], [0, null, null]], [0, null, null]]]

Output
[0, [1, null, null], [0, [1, null, null], null]]

'''




# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):

        def is_prune (self , root ):

            if root ==  None : # base case 1 -- root is null 
                return 0

            if not root.left  and not root.right :  # base case 2 - leaf node 
                if root.val == 0:
                    return 1
                else :
                    return 0

            left , right =  is_prune (self ,root.left) , is_prune(self , root.right) # check for right and left . 
            
            if left and right :  # if the both sides of the node have to be removed 
                root.left = None 
                root.right =  None 

                if root.val == 0:
                    return 1
                else :
                    return 0
                  
            elif left :    # if only the left is removed 
                root.left = None 
                return 0 

            elif right :  # if only the right is removed 
                root.right = None 
                return 0


        is_prune(self, root)

        return root 
