#question : 
'''
Find the mmiddle element of the linked list ;) 

'''

#approach : 
'''
maintain two pointers .. one moves one step once and the other 2 steps 
->  finally slow pointer contains the middle element 
'''
class Solution:
    def middleNode(self, head) :
        
        fast , slow = head , head 
        
        
        while fast and fast.next : 
            fast =  fast.next.next
            slow =  slow.next 
            
        return slow
        