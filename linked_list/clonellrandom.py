# question :
"""

Given a linked list with next and random pointer, clone the exact linked-list with next and random
pointer .  

"""

# Approach :
"""

-> The main problem comes when we need to link the random pointer, we have to search the whole linked
   list for that :(.
-> Even though we search , what if there are multiple same values.. so the solution to it is 
   to link the copy-node with original-node.


->  So we will solve this question in 3 steps ..  

1) Create and link the copy nodes with the original nodes as their next pointer
   ex :  1-> 2
         1-> 1(copy)-> 2 -> 2(copy)
2) Link the random pointer to the copy node using the help of original node  
   ex :  1(random link to 2 )-> 1(copy) -> 2(random link to 1 ) -> 2(copy)
         link   1(copy).random = 1(orig).random.next

3) Now extract the required linked list from the linked-list we made 
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.arb = None


class Solution:
    # Function to clone a linked list with next and random pointer.

    def copyList(self, head):

        if not head:
            return None

        # step 1 : insert nodes b/w

        temp = head

        while temp:
            next = temp.next
            temp.next = Node(temp.data)
            temp.next.next = next
            temp = next

        # link the random pointers

        iter = head
        dup = head.next

        while iter and dup:
            if iter.arb:
                dup.arb = iter.arb.next
            iter = dup.next
            if iter:
                dup = iter.next

        # break the links and get the ll back

        sentinal = Node(-1)
        copy = sentinal
        iter = head

        while iter:
            front = iter.next.next
            copy.next = iter.next
            iter.next = front
            copy = copy.next
            iter = front

        return sentinal.next

