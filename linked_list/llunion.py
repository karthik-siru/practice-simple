#question : 
'''
Given two sorted linked lists node0, and node1, 
return a new sorted linked list containing the union of the two lists.
'''

#approach : 
'''
IF both the values are same .. move both the pointers ..take any of them 
'''

class Solution:
    def solve(self, ll0, ll1):

        if not ll0 : 
            return ll1 
        if not ll1 : 
            return ll0 

        if ll0.val == ll1.val : 
            newhead = ll0
            ll0 = ll0.next
            ll1 = ll1.next 
        elif ll0.val < ll1.val :
            newhead = ll0
            ll0 = ll0.next
        else : 
            newhead = ll1 
            ll1 =  ll1.next 
        
        
        temp  = newhead 

        while ll0 and ll1 : 
            if ll0.val < ll1.val  :
                temp.next  = ll0 
                ll0 = ll0.next 
            elif ll0.val > ll1.val : 
                temp.next = ll1
                ll1 =  ll1.next 
            else : 
                temp.next = ll0 
                ll0 = ll0.next 
                ll1 = ll1.next 

            temp = temp.next 

        if ll0 : 
            temp.next = ll0 
        else : 
            temp.next = ll1 


        return newhead 