
'''
   Traverse each node, keeping track of its position along the X axis. Store each position X into a Set, since it holds only unique integers. We can do this with DFS having 2 params -> node & positionX.

Finally after traversing all nodes (and storing all unique positions via the set), return the size of the set .

'''

def solve(self, root):
        lines = set()

        def dfs(root, x):
            nonlocal lines
            if not root:
                return
            lines.add(x)
            dfs(root.left, x - 1)
            dfs(root.right, x + 1)

        dfs(root, 0)
        return len(lines)
