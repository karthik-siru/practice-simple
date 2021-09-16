# question :
"""
 Given a root of a tree, return the zig-zag order traversal of the tree . 
 i.e .. from left to right in one level and right to left in next level
"""

# approach :
"""
->  Get the values of the nodes by level 
->  Now append the values according to the level in normal order or reverse order
"""

from collections import deque


class Solution:
    def zigZagTraversal(self, root):

        # variables to store levels and res
        levels = []
        res = []

        q = []
        q.append(root)

        # this is to get the elements by level
        while q:
            size = len(q)
            i = 0
            a = []
            while i < size:
                Node = q.pop(0)
                i += 1
                a.append(Node.data)
                if Node.left:
                    q.append(Node.left)
                if Node.right:
                    q.append(Node.right)

            levels.append(a)

        # reverse the levels to get result

        for i in range(len(levels)):
            if i % 2 == 0:
                res.extend(levels[i])
            else:
                res.extend(levels[i][::-1])

        return res


# A better approach :
"""
-> Instead of storing the values by level and adding them to list , we can directly add them.
"""


class Solution:
    def zigzagTraversal(self, root):

        if not root:
            return []
        res = []
        q = deque()
        flag = 0

        q.appendleft(root)

        while q:
            size = len(q)
            i = 0
            if flag:
                while i < size:
                    i += 1
                    Node = q.popleft()
                    res.append(Node.data)
                    if Node.left:
                        q.append(Node.left)
                    if Node.right:
                        q.append(Node.right)
            else:
                while i < size:
                    i += 1
                    Node = q.pop()
                    res.append(Node.data)
                    if Node.right:
                        q.appendleft(Node.right)
                    if Node.left:
                        q.appendleft(Node.left)

            flag = not flag

        return res

