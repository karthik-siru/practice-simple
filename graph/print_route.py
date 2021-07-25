#qUESTION :
'''
Print the path b/w src and dest if exits . 
'''

#aPPROACH :
'''

we use path stack , we append all the  vertices , we encountered
in a recursive way  .

Now , we try eploring the graph using dfs and if we didn't find the 
dest node in any of the dfs , then we  remove the node from the path .

else , we will return False . 

-> If it is True path contains our reqired result 
-> else , no path exists .;

'''


from collections import defaultdict , deque 

class Solution :

    def __init__(self, vertices ) -> None:
        self.v = vertices 
        self.graph = defaultdict(list)

    def printDfs(self, src, dest ,visited ,path ):
       # visited is to stop already visited nodes 
        visited[src]  = True 

        path.append(src)

        # if we reached the destination , we are done .
        if src == dest :
            return True  
        
        # explore the adj nodes of the src recursively 
        for v in self.graph[src] :
            if not visited[v] :
                if self.printDfs(src , dest ,visited , path ) :
                    return  True  
        # no route find with src included in it .
        path.pop(src)

        return False 

    
    def mainDfs(self , src , dest ):
        visited = [False]*(self.v)
        path =  deque()
        if self.printDfs(src , dest , visited , path ):
            print(f"the path from  {src}  and {dest}   is : {list(path)}" )
