#question : 
'''
Rotate a double linked-list by k .
Ex :  a <-> b <-> c <-> d <-> e 

Output  c <-> d <-> e <-> a <->b 
'''

class Solution : 

    def rotatebyK(self, head , k) : 

        temp  = head 
        #move upto k nodes 
        while k and temp : 
            k -= 1 
            temp =  temp.next 
        #remove link b/w k & k+1 th node 
        temp.prev.next =None 
        temp.prev =  None 
        
        # set the new head 
        newhead  =temp 
        while temp and temp.next : 
            temp =  temp.next 
        #link  at the end 
        temp.next = head 
        head.prev = temp 

        return newhead 

