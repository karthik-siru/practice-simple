
class Solution :

    def first_repeated_word(self, s):
        l =  s.split(' ')

        if len(l)<1 :
            return "No repeated word "
        
        s = set()

        for i in l :
            if i in s :
                return i
            else :
                s.add(i)
        return "No repeated word found"

a =  Solution()

print(a.first_repeated_word(input('input the string ')))