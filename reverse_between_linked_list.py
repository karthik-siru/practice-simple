'''

   Given the head of a singly linked list and two integers left and right where left <= right,
   reverse the nodes of the list from position left to position right, and return the reversed list.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right :
            return head 
        
        count = 1
        temp , front =  head , None 
        
        while count < left :
            front = temp 
            temp  = temp.next
            count += 1
            
        current , prev = temp , None 
        
        while count <= right :
            next = current.next
            current.next = prev 
            prev = current
            current = next
            count += 1
        
        temp.next =  current
        if front:
            front.next = prev            
        else :
            return prev 
        
        return head 
