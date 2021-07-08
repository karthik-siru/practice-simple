'''
  Algorithm : 
      So , we will select a string , and try to search in the remaining words,
      for an anagram .

      In order to not to repeat the searched strings , we will use an array called 
      used[] , which default value is 1 , if any anagram of it found , or searhed . 
      the used[i] will be setto 0  . 

      we will eventually , append all the elements to the same group. 
'''

def Anagrams(words,n):
    '''
    words: list of word
    n:      no of words
    return : list of group of anagram {list will be sorted in driver code (not word in grp)}
    '''
    
    #code here
    
    l = []
    temp = []
    used = [1]*n 
    
    for i in range(n) :
        if used[i] :
            temp.append(words[i])
            sorted_s =  sorted (words[i])
            used[i] = 0 
            
            for j in range(i+1, n):
                if sorted_s  == sorted( words[j] ) :
                    used[j] = 0 
                    temp.append(words[j])
            l.append(temp)
            temp = []
            
    l= sorted(l , key = lambda  i :  words.index(i[-1]))
    return l 