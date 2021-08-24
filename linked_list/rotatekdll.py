class Node : 
    def __init__(self, data ):
        self.val =  data 
        self.next = None 
        self.prev = None 

    
class Solution :

    def rotateDllbyK (self, head , k): 
        curr , prev , next = head ,None ,None 
        count = 0
        # rotate k nodes | 
        # or untill curr becomes null 
        while curr and count < k : 
            count += 1 
            next = curr.next
            curr.next = prev 
            # link prev if not null 
            if prev :
                curr.next.prev = curr 
            prev =  curr 
            curr =  next 
        # reccur for the remaining linked-list 
        if next : 
            head.next = self.rotateDllbyK( next , k )
            head.next.prev = head 
        # return new-head 
        return prev 

    def printList(self, head): 
        temp =  head 
        while temp : 
            print(temp.val , end = " ")
            temp =  temp.next 



if __name__ == "__main__" : 
    head =  Node(1)
    temp = head 
    for i in range(2,10) : 
        temp.next = Node(i)
        temp.next.prev =  temp 
        temp  = temp.next

    a = Solution()
    print("Original-List : ")
    a.printList(head)

    head = a.rotateDllbyK(head , 3)

    print("\nRotated by 3 : ")
    a.printList(head)
    print()


