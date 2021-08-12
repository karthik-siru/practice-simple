#question  
'''
Given a binary tree root, return the number of unique vertical lines that can be drawn such that every node has a line intersecting it. Each left child is angled at 45 degrees to its left, while the right child is angled at 45 degrees to the right.

For example, root and root.left.right are on the same vertical line.

Constraints

    1 ≤ n ≤ 100,000 where n is the number of nodes in root

Example 1:

Input

       root = [1, [2, [3, null, null], null], [4, null, [5, null, null]]]

Output

       5

'''

'''
   Traverse each node, keeping track of its position along the X axis. Store each position X into a Set, since it holds only unique integers. We can do this with DFS having 2 params -> node & positionX.

Finally after traversing all nodes (and storing all unique positions via the set), return the size of the set .

Note::: I found this good approach in binary_search ... 

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
