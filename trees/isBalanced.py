# question :
"""
->  Given a root of the tree , return whether the tree is  height-balanced or not ?
->  Height-Balance means the height diff b/w subtrees must be < 1 
"""

# approach :
"""
-> Simply calculate the height of every node and determine the balance 
-> But this will be very repetetive.
-> So we will use PostOrder Traversal , to get the both left and right heights 
   and then decide .
"""


class Solution:
    def isBalanced(self, root):
        def isHeightBalanced(root, isBal=True):

            if root is None or not isBal:
                return 0, isBal

            # get the height of the left subtree
            left_height, isBal = isHeightBalanced(root.left, isBal)
            # get the height of the right subtree
            right_height, isBal = isHeightBalanced(root.right, isBal)

            # tree is unbalanced if the absolute difference between the height of
            # its left and right subtree is more than 1
            if abs(left_height - right_height) > 1:
                isBal = False

            # return height of subtree rooted at the current node
            return max(left_height, right_height) + 1, isBal
        height, res = isHeightBalanced(root, 1)
        return res

