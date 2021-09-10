# question :
"""
->  Given a root of a binary tree, return the mirror of the tree. 
"""

# approach :
"""

->  As usual , let's find out what we can do if we have the mirror of left and right subtrees 
    We can simply swap the left and right ... 

-> Base Case : --> Null Node 
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def mirror(self, root):
        def mirror_tree(node):
            # Base Case
            if node is None:
                return node

            mirror_tree(node.left)
            mirror_tree(node.right)
            # swapping left and right
            node.left, node.right = node.right, node.left

            return node

        return mirror_tree(root)

