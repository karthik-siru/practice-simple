'''

# thought process :

Start the two pointers from both ends , and maintain a left_max and right_max 

when you found a pole/hill greater than left_max  :
         update the left_max 
same with the right 

when you find a pole/hill less than the left_max :
         add the difference of left_max-pole to the result 
same with the right 


Finally .. note that if the left_max is greater than right_max .. we cannot hold water.

'''

l = [int(i) for i in input().split(" ")]

if len(l) < 3 :
    print(0)
n =  len(l)
a , b = 0 ,n-1 
left_max , right_max = 0 , 0
rain_water = 0

while a <= b :
    if l[a] < l[b]:
        # if the current pole is greater than left_max
        if l[a] > left_max :
            left_max = l[a]
        else :
            rain_water += left_max - l[a]
        a += 1 
    else :
        if l[b] > right_max :
            right_max = l[b]
        else :
            rain_water += right_max - l[b]
        b -= 1

print(f'Amount of rain_water trapped is : {rain_water}')



#another way of doing this :

'''
  We will decide which pointer to move .. either left or right according to the 
  left_max and right_max 
  
  if left_max  <  right_max :
       we can add the water to the left and move the left pointer 
  else :
       add to the rain_water and move the right pointer 

'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        a ,b = 0, n -1
        left_max , right_max = 0, 0
        rain_water = 0
        
        while a < b :
            if height[a] > left_max :
                left_max =  height[a]
            if height[b] > right_max :
                right_max = height[b]
            if left_max < right_max :
                rain_water += left_max-height[a]
                a += 1
            else :
                rain_water += right_max - height[b]
                b-= 1
        return rain_water
