# question :
"""

Return the height of the tree . 
"""

# approach :
"""
->  The first thing to do while solving tree problems is that , check whether you can solve the 
    question, if you know that you can solve left and right nodes 
->  Set up the base cases --> None or leaf Node 


-----------------------------

-> Height is max of the (left and right )+ 1 
-> base case is null node have height 0 .

"""


class Solution:
    # Function to find the height of a binary tree.
    def height(self, root):
        # code here

        def calc_height(node):
            # base case
            if not node:
                return 0
            # recursive relation
            return 1 + max(calc_height(node.right), calc_height(node.left))

        return calc_height(root)
