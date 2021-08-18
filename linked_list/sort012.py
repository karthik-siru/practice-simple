#question : 
'''
Given a linked list with 0,1,2 .. return the sorted linkedlist .
'''

#approach : 
'''
-> count the number of zeros , ones and twos in the linked-list 
-> Now change the values to 0 starting from the head .. 
   untill count_0 becomes 0 .. similarly for the ones and twos.
'''

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        count_0 , count_1, count_2 = 0, 0, 0  
        
        temp =  head 
        # loop to count 0,1,2
        while temp : 
            if temp.data == 0: 
                count_0  += 1 
            elif temp.data ==  1 : 
                count_1 += 1 
            else : 
                count_2 += 1 
            temp =  temp.next      
            
        temp  = head 
        # loop to change the values 
        while temp : 
            if count_0 > 0 : 
                temp.data = 0 
                count_0 -= 1 
            elif count_1 > 0 : 
                temp.data = 1
                count_1 -= 1 
            else : 
                temp.data = 2
                count_2 -= 1 
                
            temp =  temp.next 
            
        return head 