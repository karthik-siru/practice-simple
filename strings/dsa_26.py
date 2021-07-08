'''
Algorithm :   
   The algorithm is pretty simple , It is called vertical scanning . ;)

'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        i = 0 
        s =  strs[0]
        lcp = ""
        while i < len(strs[0]):
          
            for j in range(1, len(strs)):
                    k =  strs[j]
                    if i >= len(k) :
                        return lcp 
                    elif k[i] !=  s[i] :
                        return lcp
                    else:
                        pass 
            lcp += s[i]
            i +=  1 
            
        return lcp 