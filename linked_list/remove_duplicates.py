
'''

Given a singly linked list node, remove nodes with duplicate values while maintaining relative order of the original list.

Constraints

n ≤ 100,000 where n is the number of nodes in node

'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

# space complexity -  O(n) ,  Time Comlexity - O(n)

class Solution:
    def solve(self, node):

        if not node:
            return node
        l = set()
        l.add(node.val)
        prev = node
        temp = node.next

        while temp:
            if temp.val not in l:
                l.add(temp.val)
                prev = prev.next
            else:
                prev.next = temp.next

            temp = temp.next
        return node
