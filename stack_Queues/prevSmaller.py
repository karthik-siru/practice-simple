def leftSmaller(self, arr,n): 
        stack = []
        
        res = [0 for i in range(n)]
    
        
        for i in range(n):
            
            while stack and  arr[stack[-1]] >= arr[i] :
                stack.pop()
                
            if not stack : 
                res[i] = 0
                
            else : 
                index =  stack[-1]
                res[i] = index + 1
                
            stack.append(i)
                
        return res 
                