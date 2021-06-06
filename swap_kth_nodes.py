
'''

You are given a singly linked list node and an integer k. Swap the value of the k-th (0-indexed) node from the end with the k-th node from the beginning.

Constraints

1 ≤ n ≤ 100,000 where n is the number of nodes in node
0 ≤ k < n

example :

Input:
node = [1, 2, 3, 4, 5, 6]
k = 1

Output :

[1, 5, 3, 4, 2, 6]

'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):

        front  =  node 
        back =  node 
        back_fast = node 
        
        count = 0

        while back_fast :

            if count < k :
                front = front.next
                count += 1
            else :
                prev = back
                back = back.next

            back_fast = back_fast.next

        prev.val , front.val = front.val , prev.val 

        return node
