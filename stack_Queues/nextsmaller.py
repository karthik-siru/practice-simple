#question : 
'''
Given an array arr[ ] of size N having distinct elements, 
the task is to find the next smaller element for each element of the array 
in order of their appearance in the array.
Next smaller element of an element in the array is the nearest element 
on the right which is smaller than the current element.
If there does not exist next smaller of current element, 
then next smaller element for current element is -1. 
For example, next smaller of the last element is always -1.
'''

#approach : 
'''
->  Append the element's index into the stack ..if the current value is 
    greater than the top of the stack . 
->  If the current element is less than or equal to top of the stack .. pop the 
    index and store the current value as it's next smaller element. 

->  After iterating .. if there are any elements in the stack .. they belong to
    the no next smaller element category .. just pop them all and assign -1  
'''


class Solution:
    def nextSmallerElement(self,arr,n):
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