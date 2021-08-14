#question : 
'''
 Given a linked_list head , say whether it is cyclis or not ;) 
'''

#approach : 
'''
maintain two pointers , one is fast and the other is slow .. if they
ever meet in the linked list .. then the linked-list is cyclic . 
'''

class Solution : 

    def isCircular(head):
    # Code here
    
        fast , slow =  head , head 
        
        while fast and fast.next : 
            fast  = fast.next.next 
            slow  = slow.next 
            
            if fast == slow : 
                return 1 
                
        return 0 