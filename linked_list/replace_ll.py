#question : 
'''
You are given two linked lists a and b as well as integers lo and hi.

Remove a's nodes from indices (0-indexed) [lo, hi] inclusive and insert b in this place.
'''

#constarints :
'''
Constraints

0 ≤ n ≤ 100,000 where n is the number of nodes in a
0 ≤ m ≤ 100,000 where m is the number of nodes in b
'''

class LLNode:
    def __init__(self, data ) -> None:
        self.val = data 
        self.next = None 


class Solution:
    def solve(self, a, b, lo, hi):

        sentinal = LLNode(-1)

        sentinal.next = a 
        temp1 = sentinal
        temp2 = b 

        while temp2 :
            last = temp2
            temp2 =  temp2.next 
        
        li_prev , hi_next = sentinal , None 
        count = -1

        while temp1  : 
            if count == lo - 1  :
                li_prev = temp1 
            if count == hi+1 :
                hi_next = temp1 
            count += 1 
            temp1 = temp1.next 

        if not b : 
            li_prev.next =hi_next 
            return sentinal.next 

        li_prev.next = b
        last.next = hi_next 

        return sentinal.next 