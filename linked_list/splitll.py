
class Solution:
    def splitList(self, head, head1, head2):
        #code here
        slow_ptr = head
        fast_ptr = head
     
        if head is None:
            return
         
        # If htere are odd nodes in the circular list then
        # fast_ptr->next becomes head and for even nodes
        # fast_ptr->next->next becomes head
        while(fast_ptr.next != head and
            fast_ptr.next.next != head ):
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
 
        # If there are even elements in list then
        # move fast_ptr
        if fast_ptr.next.next == head:
            fast_ptr = fast_ptr.next
 
        # Set the head pointer of first half
        head1 = head
 
        # Set the head pointer of second half
        if head.next != head:
            head2 = slow_ptr.next
 
        # Make second half circular
        fast_ptr.next = slow_ptr.next
     
        # Make first half circular
        slow_ptr.next = head
        #this is to emulate pass by reference in python please don't delete below line.
        return head1,head2