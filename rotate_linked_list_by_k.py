'''

 Intuition

First, we need to find the previous node of the pivot one. What if the pivot node is the head? So, we need a dummy node point to the head.
Second, rotate it.


Implementation

Let the dummy node points to the node, and define the head and end for the previous node of the pivot one and the end of the list.
If k==0 means head doesn't move, that is, head == dummy; If k== len(list) means the head moves with the end together, that is, head == end.
At the last, swap the head and end


'''
def solve(self, node, k):
        firstNode = node
        firstK = k
        count = 0
        lastNode = node
        while node.next:
            if k > 0:
                k = k - 1
            else:
                lastNode = lastNode.next
            node = node.next
            count = count + 1

        if count == firstK - 1 or firstK == 0:
            return firstNode

        newFirst = lastNode.next
        lastNode.next = None
        node.next = firstNode
        return newFirst
