#approach :
'''
The idea is simple , find out number of connected components in the graph .

IF we connect them using the prev wire from the other , will save us.

SO we are interested in finding the number of connected components .

'''
from . import conc_comp_number


def minNumberOfConnections ( n , connections ) :

    if len(connections) <  n-1 :
        return -1 

    # make a graph 
    g = conc_comp_number.Solution(n)

    for i,j  in connections : 
        g.addEdge(i,j)
    
    # the min no.of changes needed is
    # number of connected components -1 

    return g.numberofConnectedComponents()-1 

