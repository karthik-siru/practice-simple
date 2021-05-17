
'''
  
  Reverse a linked list inplace .. we can do that in both recursive and iterative ways . 
  
  recurcive method requires O(n) -- recursive stack  and O(n) time complecxity
  
  iterative  -- space complexity-  O(1) , Time complexity - O(n)
  

'''

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):

        if not node or not node.next :
            return node 
        p =  LLNode(0)
        p =  self.solve(node.next)

        node.next.next = node 
        node.next =  None 
        return p 

        # iterative method :

       '''
        current , prev = node , None 

        while current :
            temp = current.next 
            current.next = prev 
            prev =  current 
            current = temp

        return prev 

        '''    
