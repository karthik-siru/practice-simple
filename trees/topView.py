# question :
"""
->  Given a root of a binary tree, return the top view of a tree.
"""


# approach :
"""
-> Let's store the node.values and their values according to their horizontal distance from the 
   root. 
-> Root has a distance 0  
-> And let's go with preorder traversal. 

-> Update the dictionary, if we found any new distance or we found the distance with less level 

"""


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):
        def PrintTop(root, dist, level, dict):

            if root is None:
                return None
            # update if we are at new distance
            # or we find the same distance with less level
            if dist not in dict or level < dict[dist][1]:
                dict[dist] = [root.data, level]
            # Preorder..
            PrintTop(root.left, dist - 1, level + 1, dict)
            PrintTop(root.right, dist + 1, level + 1, dict)

        dict = {}

        PrintTop(root, 0, 0, dict)

        res = []
        # print the keys according to dist from root.
        for key in sorted(dict.keys()):
            res.append(dict[key][0])

        return res

