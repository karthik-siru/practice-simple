
#approach : 
'''
->  let's maintain two counters left_count and right_count ... 
->  traverse the string from the left .. increase the count accordingly.
->  In any case ..
      * right_count < left_count  ..  '....((( )' we are here  
      * right_count == left_count .. it means we are having a valid
        substring now .  Update the max__length 
      * right_count > left_count  ...   '()(()))'.. this is invalid 
        make the counts 0

-> Similarly for while traversing from the right to left . 

'''
class Solution:
    def findMaxLen(ob, s):
        # code here
        # traverse from left-right 
        l,r = 0,0
        max_ = 0
        for i in range(len(s)):
            if s[i] == '(':
                l +=1
            else:
                r +=1
            if l == r:
                max_ = max(max_, 2 * r)
            else:
                if r >= l:
                    l = r = 0
        # traverse from right-left 
        l,r = 0,0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '(':
                l += 1
            else:
                r += 1
            if l == r:
                max_ = max(max_, 2 * l)
            else:
                if l >= r:
                    l = r = 0
        return max_