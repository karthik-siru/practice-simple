class Solution : 

    def Sumpairssdll(self, head , target ): 
        if head is None :
            return head
        front =  head 
        back = head 
        # get the end node 
        while back.next  : 
            back = back.next 
        res = []
        #traverse untill the both collide 
        while front != back : 
            val = front.data + back.data
            if val <  target : 
                front  =  front.next
            elif val >target  :
                back =  back.prev 
            else : 
                res.append((front.data , back.data ))

        return res 
        
    