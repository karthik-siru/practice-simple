#qUUESTION : 
'''
Given a node , give me the clone of a graph . 
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:

    def cloneGraph(self, node) -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        queue = deque([node])

        while queue:
            node = queue.popleft()

            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
                    
        return nodeCopy
        