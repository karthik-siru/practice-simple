class avlNode :
    
    def __init__(self , val ) -> None:
        self.val = val
        self.left = None 
        self.right =None 
        self.height =  0 

class avlTree :
    
    def __init__(self) -> None:
        self.root = avlNode()

    def height(self, node ) : 
        if node :
            return node.height 
        return 0
    
    def balanceFactor(self, node):
        if node :
            abs(self.height(node.left) -
                self.height(node.right))
        return 0 

    def leftRotate(self, node ):
        a = node
        b = node.right 
        #rotations 
        a.right =  b.left
        b.left =  a

        #update heights
        a.height = 1 + max(self.height(a.left) , 
                           self.height(a.right))
        b.height =  1 + max(self.height(b.left),
                             self.height(b.right))
        return b 
    
    def rightRotate(self, node ):
        a  = node 
        b  = node.left
        #rotations 
        a.left = b.right 
        b.right = a 

        #update heights 
        a.height = 1 +  max( self.height(a.left)  , 
                             self.height(a.right))
        b.height = 1 + max(  self.height(b.left) , 
                             self.height(b.right))
        return  b 
    
    def minNode(self, node ):
        temp = node 
        while temp and temp.left :
            temp =  temp.left  
        return temp

    def maxNode(self, node ):
        temp = node 
        while temp and temp.right :
            temp =  temp.right  
        return temp

    def insertNode (self ,root ,key):
        if not root :
            return avlNode(key)
        elif root.val >  key :
            root.left = self.insertNode(root.left , key)
        else :
            root.right = self.insertNode(root.right ,key)

        #update heights of the ansestor
        root.height =  1 + max( self.height(root.left),
                                self.height(root.right)
                              )

        balancefactor =  self.balanceFactor(root)

        # left-left
        if(balancefactor>1 and self.balanceFactor(root.left) >=0):
              return self.rightRotate(root)
        # left-right 
        elif (balancefactor>1 and self.balanceFactor(root.left)<0):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        #right -right 
        elif (balancefactor<-1 and self.balanceFactor(root.right)<=0 ):
            return self.leftRotate(root)
        
        # right -left
        elif (balancefactor<-1 and self.balanceFactor(root.right)>0 ):
            root.right =  self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return  root

    def deleteNode(self,root , key):
        if not root :
            return root 

        if root.val > key :
            root.left = self.deleteNode(root.left , key)
        
        elif root.val < key :
            root.right = self.deleteNode(root.right , key)
        #found the node with value key 
        else : 
            #if only one child or no child 
            if not root.right :
                temp = root.left
                root = None 
                return temp
            elif not root.left:
                temp = root.right 
                root = None 
                return temp 
            #two children case 

            else :
                temp = self.minNode(root.right)

                root.val = temp.val
                
                root.right = self.deleteNode(root.right , temp.val)

        if not root :
            return root 
        
        #update heights of the ansestor
        root.height =  1 + max( self.height(root.left),
                                self.height(root.right)
                              )

        balancefactor =  self.balanceFactor(root)

        # left-left
        if(balancefactor>1 and self.balanceFactor(root.left) >=0):
            return self.rightRotate(root)
        # left-right 
        elif (balancefactor>1 and self.balanceFactor(root.left)<0):
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        #right -right 
        elif (balancefactor<-1 and self.balanceFactor(root.right)<=0 ):
            return self.leftRotate(root)
        
        # right -left
        elif (balancefactor<-1 and self.balanceFactor(root.right)>0 ):
            root.right =  self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return  root

    def search(self, key  ):
        temp = self.root 

        while temp : 
            if temp.val == key :
                return temp
            elif temp.val > key :
                temp = temp.left 
            else :
                temp = temp.right 

        return None

    def printTree(self,node ):
        if node :
           self.printTree(node.left)
           print(node.val, end ="")
           self.printTree(node.right)  

    def isBst(self, root ):
        if not root :
            return True 
        if not root and root.val < self.maxNode(root.left):
            return  False 
        if not root and root.val > self.minNode(root.right):
            return  False
        
        if not self.isBst(root.left) or not self.isBst(root.right):
            return 0 

        return 1 

    def isAvl(self, node ):
        if node :           
            if self.isBst(node) :
                
                if self.isAvl(node.right) and self.isAvl(node.left):

                    k = self.balanceFactor(node)

                    if k >= -1 and k<=1 :
                        return True 

        return False 
        