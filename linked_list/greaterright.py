#question : 
'''
- > Replace the nodes in linked-list.. with the nodes greater than it's value on
right side . 
'''

#approach : 
'''
->  Since there is a chance of changing the head .. we will use a sentinal node .
->  let us make three variables 
    1) prev  ----> previous node --->  sentinalnode 
    2) temp  ----> iterator      --->  head 
    3) temp2 ----> right-iterator -->  None 

->  Set the temp value as key ... iterate through the right of the linked-list
    using temp2 variable 
->  If any node found --> change the prev->next to temp2 ---> set temp = temp2 
->  if not found .. temp2 will be None -> then step up prev and temp iterators 
->  Finally return the sentinal.next 
'''


class Node : 
    def __init__(self,data ) : 
        self.data =  data 
        self.next = None 

class Solution:
    def compute(self,head):
        # sentinal--> dummy head 
        sentinal = Node(-1)
        sentinal.next = head 
        #initialise the variables 
        temp =  head 
        prev = sentinal 
        #iterate over the linked-list
        while temp : 
            key =  temp.data 
            temp2 = temp.next 
            # search in the right of the node 
            while temp2 : 
                if temp2.data > key : 
                    prev.next = temp2 
                    temp = temp2 
                    break 
                temp2 =  temp2.next 
            # not found.. step up prev,temp
            if not temp2 :
               temp =  temp.next 
               prev =  prev.next 
                
        #return sentinal.next         
        return sentinal.next