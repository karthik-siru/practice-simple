


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):

        current , prev , next =  node , None , None 
        count = 0

        while current and count < k :
            next = current.next
            current.next = prev 
            prev = current 
            current =  next 
            count += 1
        
        # be careful if you send the null node to solve .. it will run forever .
        if next :
            node.next =  self.solve(current , k)

        return prev
   
