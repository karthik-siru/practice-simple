class Solution:

    def rev(self, head):
  
        pre = None;
        curr = head;
        nex = curr.next;
    
        # Till current is not None
        while (curr):
            curr.next = pre;
            pre = curr;
            curr = nex;
            nex = (curr.next) if curr else None
        
        head = pre
        return head

    def solve(self, head):
        if (head == None):
           return None;
  
        # Dummy Node
        res = LLNode(-1);
        temp = res;
    
        # Reverse the LL
        head = self.rev(head);
        st = []
    
        while (head):
    
            # Initial Condition
            if (len(st) == 0):
                temp.next = LLNode(0);
                st.append(head.val);
            
            else:
    
                # Maintain Monotonicity
                # Decreasing stack of element
                while (len(st) != 0 and st[-1]<= head.val):
                    st.pop();
    
                # Update result LL
                if (len(st) == 0):
                    temp.next = LLNode(0);
                    st.append(head.val);
                
                else:
                    temp.next = LLNode(st[-1]);
                    st.append(head.val);
                
            head = head.next;
            temp = temp.next;
  
        # Delete Dummy Node
        temp = res;
        res = res.next;
        del temp;
    
        # Reverse result LL
        res = self.rev(res);
        return res;
