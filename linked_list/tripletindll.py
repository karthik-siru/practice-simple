class Node : 
    def __init__(self , data ) -> None:
        self.val =  data 
        self.next = None 
        self.prev = None

class Solution : 

    def countTriplets(self, head , target): 
        if not head : 
            return 0 
        end = head 
        #store end node 
        while end and end.next :
            end =  end.next
        # temp as iterator 
        temp = head 
        count = 0

        while temp  :
            # left & right pointers
            left = temp.next
            right = end 
            # k -> new target 
            k =  target- temp.val 
            while left.val < right.val : 
                # if found ..break 
                 if left.val + right.val == k :
                     count += 1 
                     break 
                # increment left & decrement right 
                 left =  left.next
                 right =  right.prev
            temp =  temp.next 

        return count 