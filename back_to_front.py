
'''

Given a singly linked list node, reorder it such that we take: the last node, and then the first node, and then the second last node, and then the second node, etc.

Can you do it in \mathcal{O}(1)O(1) space?


Example 1
Input

node = [0, 1, 2, 3]
Output

[3, 0, 2, 1]

'''


# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse (self , head ) :
        current = head 
        prev , next = None , None 

        while current :
            next = current.next
            current.next = prev
            prev = current 
            current = next
        return prev 



    def solve(self, node):
        if not node  or not node.next:
            return node 
        
        fast , slow , prev  =  node , node , None 

        while fast  and fast.next :
            prev = slow 

            fast = fast.next.next
            slow =  slow.next 
        
        slow = self.reverse(slow)
        prev.next = None 

        res =  LLNode (0)
        temp = res 

        temp1 , temp2 =  node , slow 
        i = 0

        while temp1 and temp2 :
            if i == 0 :
                temp.next = temp2 
                temp2 = temp2.next
                temp =  temp.next
                i = 1
            else :
                temp.next =  temp1
                temp1 = temp1.next
                temp = temp.next
                i = 0
        if temp2 :
            temp.next = temp2 
        if temp1 :
            temp.next =  temp1 
        return res.next

