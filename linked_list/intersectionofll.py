#question : 
'''
Given two lists sorted in increasing order, create a new list
representing the intersection of the two lists.
The new list should be made with its own memory — 
the original lists should not be changed.

Example : 

a.  1->2->3->4->5
b.   2->2->5

Output : 2->5 

'''

class Node :
    def __init__(self, value ) -> None:
        self.data = value 
        self.next =None 
class Solution : 
    def findIntersection(self,head1,head2):
        #return head
        
        s1 =  set()
        
        temp =  head1  
        
        while temp :
            s1.add(temp.data)
            temp =  temp.next 
            
        temp =  head2 
        
        newHead = None 
        nt =  newHead 
        
        while temp : 
            if temp.data in s1 : 
                s1.remove(temp.data)
                if not nt :
                    nt = Node(temp.data)
                    newHead = nt 
                else : 
                    nt.next = Node(temp.data)
                    nt =  nt.next 
                    
            temp =  temp.next 
            
            
        return newHead 
