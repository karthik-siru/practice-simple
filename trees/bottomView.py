# approach :
"""
->  Same as top view , we have to update when we found a distance with same or greater level 
"""


class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def bottomView(self, root):
        def PrintBottom(root, dist, level, dict):

            if root is None:
                return None
            # update if we are at new distance
            # or we find a level less than distance level
            if dist not in dict or level >= dict[dist][1]:
                dict[dist] = [root.data, level]
            # Preorder..
            PrintBottom(root.left, dist - 1, level + 1, dict)
            PrintBottom(root.right, dist + 1, level + 1, dict)

        dict = {}

        PrintBottom(root, 0, 0, dict)

        res = []
        # print the keys according to dist from root.
        for key in sorted(dict.keys()):
            res.append(dict[key][0])

        return res
