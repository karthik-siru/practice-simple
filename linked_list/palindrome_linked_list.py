#question : 
'''
Given a singly linked list node whose values are integers,
 determine whether the linked list forms a palindrome.
'''


'''
my solution 
'''
def solve(self, node):

        a = []
        temp = node
        while temp :
            a.append(temp.val)
            temp = temp.next

        return a[::-1] == a  
      
# can we do this using O(1) space complexity 


'''

 Intuition:

  Find the middle node, then reverse the right part, loop the left and the right part meanwhile to check it.
  
Implementation :

Use fast-slow pointers to locate the middle node.
Reverse the right part.check it


Time Complexity :

All of the three while-loop phases are O(n). Thus, the total time complexity is O(n).
Space Complexity

We're just use serval node point, so the space complexity is O(1)



'''



# without using extra space :::

def solve(self, node):
        fast, slow = node, node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        right = None
        while slow:
            p = slow.next
            slow.next = right
            right = slow
            slow = p

        left = node
        while left is not None and right is not None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
