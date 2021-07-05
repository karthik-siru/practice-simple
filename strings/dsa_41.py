
class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        
        if len(str1) != len(str2 ) :
            return 0 
        
        hash_map_1 = {}
        hash_map_2 = {}
        
        for i in range(len(str1)) :
            if str1[i] not in hash_map_1:
                hash_map_1[str1[i]]  = 1
            else :
                hash_map_1[str1[i]] += 1 
            
            if str2[i] not in hash_map_2 :
                hash_map_2[str2[i]]  = 1
            else :
                hash_map_2[str2[i]] += 1 

        for i in range(len(str1)) :
            if hash_map_1[str1[i]] !=  hash_map_2[str2[i]] :
                return False 
        return True 

    
s = Solution()

result = s.areIsomorphic(input('input the first string :') , input('input the second string:'))

print(result )