#approach : 
'''
->  Same as reversing single ll .. just add prev.prev =  next ;) 
'''
def reverseDLL(head):
    #return head after reversing
    
    prev , curr = None , head 
    
    while curr : 
        next = curr.next
        curr.next = prev
        prev = curr 
        prev.prev = next 
        curr =  next 
        
    return prev 