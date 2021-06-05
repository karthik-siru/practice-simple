
'''

**Flloyd-Washal-Algorithm **


the idea is to run two pointers ,, one is slow and the other is fast 

slow will move one step per move  
fast will move two steps per move 

if the linked-list has a loop , the fast and slow pointers will meet .. 

Question-Extension :

how to get to the starting point of the loop 

after detecting the loop  

place the slow pointer to the head and now move both fast and slow one step per move 

and they will meet again .




'''


def Cycle_Detection (self, head: ListNode) -> bool:
        
        if not head: return False
        s = f = head
        
        while f and f.next:
            s, f = s.next, f.next.next
            if f is s: return True
        return False
