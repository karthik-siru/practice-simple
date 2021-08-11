
class Node : 
    def ___init__(self, data) :
        self.data =  data
        self.next =None 

class Solution:

    # this function reverses the linked list  ;) 
    def reverse (self, head): 
        
        prev , curr , next = None , head , head.next 
        
        while curr : 
            next = curr.next
            curr.next =prev 
            prev = curr 
            curr = next 
            
        return  prev 
        
    def addOne(self,head):
        #Returns new head of linked List.
        # need prev to add 1 in the cases like 999 ;) 
        head = self.reverse(head)
        k = head
        carry = 0
        prev = None
        head.data += 1
     
        # update carry for next calulation
        while(head != None) and (head.data > 9 or carry > 0):
            prev = head
            head.data += carry
            carry = head.data // 10
            head.data = head.data % 10
            head = head.next
     
        if carry > 0:
            prev.next = Node(carry)
        # Reverse the modified list
        return self.reverse(k)

