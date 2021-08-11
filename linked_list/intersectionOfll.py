
class Node : 
    def __init__(self, data) :
        self.data = data
        self.next =None 

class Solution :

    def intersetPoint(head1,head2):
        #code here
        # gives the length of the ll
        def length (head ):
            temp =  head 
            count = 0
            
            while temp : 
                count +=1 
                temp =  temp.next 
                
            return count 
        #moves the  longest uncommon  part  
        def move(head , k) :
            while k > 0 : 
                head = head.next
                k -=  1 
                
            return head         
        #find the lengths 
        l1 =  length(head1)
        l2 =  length(head2)
        #move the longest uncommon ll
        if l1 > l2 : 
            head1 = move(head1, l1-l2 )
        else : 
            head2 = move(head2 , l2-l1 )
        # iterate upto when both are same    
        while head1 !=  head2 : 
            head1 = head1.next
            head2 =  head2.next 
            
        return head1.data