
class Solution:
    #Function to sort the given linked list using Merge Sort.
    
    def merge (self, a, b) : 
        if not a :
            return b 
        elif not b : 
            return a 
            
        if a.data <  b.data : 
            result =a
            result.next =  self.merge(a.next , b)
        else : 
            result =b 
            result.next =  self.merge(a, b.next )
        return result 
        
        
    # to find the middle element 
    
    def frontBackSplit(self, source):
        if source is None or source.next is None:
            return source, None
     
        (slow, fast) = (source, source.next)
    
        while fast and fast.next :
     
            fast = fast.next.next 
            slow = slow.next
     
        ret = (source, slow.next)
        slow.next = None
     
        return ret
        
    def mergeSort(self, head):
        
        if head  is None  or head.next is None : 
            return head 
            
        front ,back = self.frontBackSplit(head )
        
        front = self.mergeSort(front)
        back = self.mergeSort(back)
        
        return self.merge(front , back )