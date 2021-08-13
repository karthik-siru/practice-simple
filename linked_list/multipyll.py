#question : 
'''
Given two numbers in Linked_list format .. multiply them ;) 

'''

def multiplyTwoList(head1, head2):
    # Code here
    
    
    modulo = 10**9 + 7
    
    def  getNumber (head ) :
        result = 0
        
        temp = head
        
        while temp : 
            result *= 10 
            result += temp.data 
            
            temp = temp.next
            
        return result 
        
    return (getNumber(head1)*getNumber(head2))%modulo