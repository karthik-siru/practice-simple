    def findNum(self, n : int):
        # Complete this function
        def check(p,n): 
          
            temp = p 
            count = 0
            f = 5
            while (f <= temp): 
                count += temp/f 
                f = f*5
          
            return (count >= n) 
            
        if (n==1): 
          return 5
   
        low = 0
        high = 5*n 
       
        # Binary Search. 
        while (low <high): 
      
            mid = (low + high) >> 1
       
            if (check(mid, n)): 
                high = mid 
            else: 
                low = mid+1
          
       
        return low 