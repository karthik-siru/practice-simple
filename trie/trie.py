class trieNode :
    def __init__ (self, char ):
        self.char =  char
        self.endWord = 0
        self.children = []
        self.count = 0

class trie :

    def __init__(self):
        self.root =  trieNode('*')

    def add_word (self,newWord) :

        node =  self.root 
        # take a temporary variable .
        
        for char in newWord :
            # check in the children of the node for same character 
            foundInChildren =  False 
            for child in node.children :
                # if found update the node and increase the count                
                if child.char == char :
                    child.count += 1 
                    node =  child 
                    foundInChildren =  True 
                    break 
            # not found , then insert a new trieNode with  that character
            # now update the node ;) 
            if not foundInChildren :
                new_node = trieNode(char)
                node.append(new_node)
                node =  new_node 

        node.endWord = 1 

    def findPrefix (self, prefix) :
        '''
        1) check whether a string exists with a prefix like this 
        2) If yes , how many such strings exists .
        '''

        node =  self.root 

        for char in prefix :
            childFound =  False 
            for child in node.children :
                if child.char == char :
                    childFound = True
                    node = child
                    break 
            if not childFound :
                return (False , 0)

        # if we are here means,that implies we found our prefix string.

        return (True , node.count)

