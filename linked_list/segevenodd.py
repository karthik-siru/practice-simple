#question : 
'''
Segregate even and odd values in the linked-list . 
'''

#approach : 
'''
Store even and odd values in seperate lists . 
-> Untill even becomes empty .. pop the front value and change the node..data
-> continue .. for add also . 
'''

class Solution:
    def divide(self, N, head):
        # code here
        even = []
        odd = []
        
        temp = head 
        
        while temp : 
            if temp.data & 1 : 
                odd.append(temp.data)
            else : 
                even.append(temp.data )
            temp =  temp.next 
        
        temp  = head         
        while temp : 
            if even : 
                temp.data = even.pop(0)
            else : 
                temp.data =  odd.pop(0)
            temp =  temp.next 
            
        return head 
            