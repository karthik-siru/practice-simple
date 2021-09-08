# question :
"""
->  Given the root of a binary tree return the diameter of the tree. 
"""

# approach :
"""
->  DIAMETER :  length of the longest path b/w any nodes. 

-> Find the heights of all the node and find the max of 
   (sum of left_height + sum of right_height +1 ).

-> That will be our max diameter.

-> I HAVE A BETTER IDEA

->  The Idea is to use postorder traversal, get the left_height and right_height and 
    keep updating the max_diameter. 
 
"""


def getDiameter(root, diameter):

    # base case: tree is empty
    if root is None:
        return 0, diameter

    # get heights of left and right subtrees
    left_height, diameter = getDiameter(root.left, diameter)
    right_height, diameter = getDiameter(root.right, diameter)

    # calculate diameter "through" the current node
    max_diameter = left_height + right_height + 1

    # update maximum diameter (note that diameter "excluding" the current
    # node in the subtree rooted at the current node is already updated
    # since we are doing postorder traversal)
    diameter = max(diameter, max_diameter)

    # it is important to return the height of the subtree rooted at the current node
    return max(left_height, right_height) + 1, diameter


def getBTDiameter(root):

    diameter = 0
    return getDiameter(root, diameter)[1]
