#question : 
'''

Find the largest rectangular area possible in a given histogram where 
the largest rectangle can be made of a number of contiguous bars. 
For simpliFind the largest rectangular area possible in a given histogram 
where the largest rectangle can be made of a number of contiguous bars. 
For simplicity, assume that all bars have the same width and the width is 
1 unit.city, assume that all bars have the same width and the width is 1 unit.

'''

#approach : 
'''

->  Think .. what the max area can be find with the current element as height 
->  What will be it's width .. ? 
->  We need to find the immeddiate smaller element in it's right and left space
->  Now .. we have our height and width .. find the max_area ... by height as 
    the other bars in the histogram.. 

'''
class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    
    def rightSmaller(self,arr,n):
        #code here 
        
        stack = []
        res = [0 for i in range(n)]
        
        for i in reversed(range(n)):
            
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
                
            if not stack : 
                res[i] = n-1 
            else : 
                res[i] = stack[-1] -1 
                
            stack.append(i)
            
        return res 
                
        
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
                
                
        
    def getMaxArea(self,histogram):
        #code here
        l = self.leftSmaller(histogram , len(histogram))
        r = self.rightSmaller(histogram , len(histogram))
        

        max_area = -99999
        
        for i in range(len(histogram)):
            max_area =  max(histogram[i] *(r[i] - l[i] + 1 ) , max_area )
            
        return max_area 