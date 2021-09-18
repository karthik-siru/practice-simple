class Solution:
    def deleteNode(self, root, key: int):
        def minNode(node):
            temp = node
            while temp and temp.left:
                temp = temp.left
            return temp

        def checkNode(root, key):
            temp = root

            while temp:
                if temp.val == key:
                    return True
                elif temp.val > key:
                    temp = temp.left
                else:
                    temp = temp.right

            return False

        def deleteNode(root, key):
            if not root:
                return root

            if root.val > key:
                root.left = deleteNode(root.left, key)

            elif root.val < key:
                root.right = deleteNode(root.right, key)
            # found the node with value key
            else:
                # if only one child or no child
                if not root.right:
                    temp = root.left
                    root = None
                    return temp
                elif not root.left:
                    temp = root.right
                    root = None
                    return temp
                # two children case

                else:
                    temp = minNode(root.right)

                    root.val = temp.val

                    root.right = deleteNode(root.right, temp.val)

            return root

        if not checkNode(root, key):
            return root

        return deleteNode(root, key)

