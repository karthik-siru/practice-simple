class Solution : 

    def movetoFront (self  , head ):
        temp = head 
        prev = None 

        while temp and temp.next : 
            prev =  temp
            temp = temp.next

        if prev : 
            prev.next =  None 
            temp.next = head 

        return temp 