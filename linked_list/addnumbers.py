
''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Node : 
    def __init__(self, data ) :
        self.data =  data 
        self.next = None 

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        
        def number (head ) : 
            temp = head 
            count = 0 
            while temp :
                count *= 10 
                count += temp.data 
                temp = temp.next
            return count 
        
        def reverse (head ) : 
            prev =  None 
            curr = head
            next = head.next 
            
            while curr : 
                next = curr.next 
                curr.next =  prev 
                prev = curr 
                curr =  next 
                
            return prev 
                
            
        num =   number(first) + number(second)
        
        newll = Node(num%10)
        num =  num//10 
        temp = newll
        
        while num :
            n = num%10 
            num = num//10 
            nextNode = Node(n)
            temp.next = nextNode 
            temp =  nextNode 
        
        return reverse(newll)