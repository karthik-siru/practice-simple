# question :
"""
->  Given a root of a binary tree .. return it's left view

ex :           1
             /   \
            3     2

Output :  1 3
"""

# approach :
"""

-> We just need the first element in all the levels. 
-> Let's maintain a count and whenever it reaches the current size , append it to the queue 
"""


def LeftView(root):

    # code here

    if not root:
        return []

    # level order traversal and first element in a level

    q = []
    q.append(root)
    res = []

    while q:

        size = len(q)
        i = 0

        while i < size:
            i += 1

            Node = q.pop(0)

            if i == 1:
                res.append(Node.data)

            if Node.left:
                q.append(Node.left)
            if Node.right:
                q.append(Node.right)

    return res

