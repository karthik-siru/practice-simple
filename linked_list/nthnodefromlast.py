#question  :
'''
Return the value of the node from the end of the linked list . 
'''

def getNthFromLast(head,k):
    #code here
    p1, p2 = head , head 
    n = k  
    count = 0
    while p2 : 
        end =  p2
        if n <= 0 : 
            p1 = p1.next 
        p2 =  p2.next 
        n-= 1 
        count += 1 
        
    if count < k :
        return -1 
        
    return p1.data   