
class bstNode :

    def __init__(self, val) -> None:
        self.val = val 
        self.left = None 
        self.right  = None 
        self.parent  = None 
        
class bst : 

    def __init__(self) -> None:
        self.root = None 
    
    # returns the min value node 
    def minNode(self, node ):
        temp = node 
        while temp and temp.left :
            temp =  temp.left  
        return temp
    
    # returns the max value node 
    def maxNode(self, node):
        temp = node  
        while temp and temp.right:
            temp = temp.right 
        return temp 
 
    # function searches and returns node , if the value exists.
    def Search(self , val ) :
        temp =  self.root 
        
        while temp :
            if temp.val > val :
                temp = temp.left 
            elif temp.val < val :
                temp = temp.right 
            else :
                return temp 
        return None 

    # insertion 
    def insertNode (self, val) :

        y =  None 
        x =  self.root 
        
        while x : 
            y =x 
            if val <  x.val :
                x =  x.left 
            else :
                x =  x.right 

        # if tree is empty 
        if y == None :
            self.root =  bstNode(val)
        else :
            new_node  =  bstNode(val)
            new_node.parent =  y 

            if new_node.val >  y.val :
                y.right =  new_node 
            else :
                y.left =  new_node 

    # successor (returns None , if no suuccessor exits )
    def successor (self, val):

        node = self.Search(val)
        # if the node  exits in the tree 
        if node :
                if node.right :
                    return self.minNode(node.right)
                else : 
                    # search for the node , which is a left node of it's parent 
                    p = node.parent 
                    
                    while p and p.right == node : 
                        node = p 
                        p =  p.parent 
                    return p 
        else :
            return f"node with value : {val} doesn't exits "

    # predecessor (returns None if no predecessor exits)
    def predecesor (self, val) :
        node =  self.Search(val)
        if node :
            if node.left :
                return self.maxNode(node.left)
            else :
                p = node.parent 

                while p and p.left == node :
                    node = p
                    p =  p.parent 
                return p
        else :
            return f"node with value: {val}  doesn't exits ."

    #transplant (replace u with v)
    def transplant (self,u,v) :

        if u.parent == None :
             self.root = v 
        elif u.parent.left == u :
             u.parent.left = v  
        else :
             u.parent.right = v 

        if v : 
            v.parent = u.parent        

    # deletions 
    def deleteNode (self,val):
        node =  self.Search(val)
        if node : 
            # if single child just move up the other child 
            if node.left ==  None : 
                self.transplant(node , node.right)
            if node.right ==  None :
                self.transplant(node , node.left)
            #two child case 
            else : 
                y = self.minNode(node.right)

                if y.parent != node : 
                    self.transplant(y , y.right)
                    y.right = node.right 
                    node.right.parent =  y  

                self.transplant( node , y)    
                y.left =  node.left
                y.left.parent = y 
            
        else :
            return f"node with value : {val}doesn't exits "

    def Inorder(self,node):
        if node :
            self.Inorder(node.left)
            print(node.val , end = " ")
            self.Inorder(node.right)
 
 
l = [4,3,2,5,1]

bstTree =  bst()

for i in l : 
    bstTree.insertNode(i)

print(bstTree.minNode(bstTree.root))
print(bstTree.maxNode(bstTree.root))
print(bstTree.Search(5).val)
print(bstTree.Search(6))
print(bstTree.successor(2).val)
print(bstTree.successor(5))
print(bstTree.successor(7))
print(bstTree.predecesor(5).val)
print(bstTree.predecesor(1))
print(bstTree.deleteNode(1))
print(bstTree.minNode(bstTree.root).val)
bstTree.Inorder(bstTree.root)
print("")