# question :
"""
Return the level order traversal of the given tree.
"""

# approach :
"""

-> Same as Breadth-First-Traversal.. store the left and right of the popped node from  queue. 
"""


class Solution:
    # Function to return the level order traversal of a tree.
    def levelOrder(self, root):
        # Code here
        res = []

        queue = []

        queue.append(root)

        while queue:
            node = queue.pop(0)
            res.append(node.data)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return res

