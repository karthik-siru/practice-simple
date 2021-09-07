# question :
"""
->  Return the array of elements containing reverse level order traversal of the given tree. 
"""

# Approach :
"""
->  Same as level-order traversal, but we have to insert at the begining everytime..  
->  And also we have to apppend right child first and then left child. 
"""


def reverseLevelOrder(root):
    # code here

    res = []

    q = []

    q.append(root)

    while q:
        node = q.pop(0)
        # append at the begining
        res.insert(0, node.data)
        # append rigt first.
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)

    return res

