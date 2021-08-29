#question : 
'''
You are given a singly linked list node and an integer k. Order the linked list so that all nodes whose values are less than k come first, all nodes whose values are equal to k next, and then other nodes last.

The relative ordering of the nodes should remain the same.

Bonus: Can you do it in \mathcal{O}(n)O(n) time and \mathcal{O}(1)O(1) space?
'''

class LLNode:
    def __init__(self, data ) -> None:
        self.val = data 
        self.next = None 


class Solution:
    def solve(self, node, k):

        # chances of change in head 
        # so we will use sentinal-node 

        front = LLNode(-1)
        temp1 = front 
        
        middle = LLNode(-1) 
        temp2 = middle 

        back = LLNode(-1)
        temp3 = back 
        
        # general iterator 
        temp = node 

        while temp : 
            next = temp.next 
            if temp.val < k: 
                temp1.next = temp
                temp1 = temp1.next
            elif temp.val > k:
                temp3.next = temp
                temp3 = temp3.next 
            else : 
                temp2.next = temp
                temp2 = temp2.next 

            temp = next 
        # making next of last node as 
        # None 
        temp3.next = None 

        # linking part 

        temp1.next = middle.next 
        temp2.next = back.next 

        return front.next 