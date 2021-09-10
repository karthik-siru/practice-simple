def RightView(root):

    # code here

    if not root:
        return []

    # level order traversal and last element in a level

    q = []
    q.append(root)
    res = []

    while q:

        size = len(q)
        i = 0

        while i < size:
            i += 1
            Node = q.pop(0)
            if i == size:
                res.append(Node.data)

            if Node.left:
                q.append(Node.left)
            if Node.right:
                q.append(Node.right)

    return res
