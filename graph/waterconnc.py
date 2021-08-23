#question : 
'''

Every house in the colony has at most one pipe going into it and at 
most one pipe going out of it. 
Tanks and taps are to be installed in a manner such that every house 
with one outgoing pipe but no incoming pipe gets a tank installed on 
its roof and every house with only an incoming pipe and no outgoing pipe 
gets a tap.

Given two integers n and p denoting the number of houses and the number of pipes.
The connections of pipe among the houses contain
three input values: ai, bi, di denoting the pipe of diameter di 
from house ai to house bi. Find the efficient way for the construction of 
the network of pipes.

The output will contain the number of pairs
of tanks and taps t installed in first line and 
the next t lines contain three integers
: house number of tank, house number of tap and the minimum diameter of pipe 
between them.

'''

#eaxmple : 
'''
Input:
n = 9, p = 6
a[] = {7,5,4,2,9,3}
b[] = {4,9,6,8,7,1}
d[] = {98,72,10,22,17,66} 


Output: 
3
2 8 22
3 1 66
5 6 10


Explanation:
Connected components are 3->1, 5->9->7->4->6 and 2->8.
Therefore, our answer is 3 followed by 2 8 22, 3 1 66, 5 6 10.
'''


#approach : 
'''
->  The plan is to use the idea of dfs .  
->  We keep track of the visited links .. to not to visit it again
->  we search for tank_value in the tap_array 
->  if found .. update the diameter 
->  if the link found is already visited .. then no need for tank or tap (closed loop)
->  same for the tap_value .. 
'''

#User function Template for python3
class Solution:
    def solve(self, n, p ,a, b, d): 
        #code here
        
        visited = [False  for i in range(p)]
        # resulting array 
        res = []
        #sets foor faster search 
        setb = set(b)
        seta = set(a)
        
        for i in range(p) : 
            
            if not visited[i] : 
                #set the new entry 
                new = [a[i] , b[i] , d[i]]
                seta.remove(a[i])
                setb.remove(b[i])
                # to loop found 
                not_found = 1 
                while new[0] in setb or new[1] in seta : 
                    # search in tap_array 
                    if new[0] in setb : 
                        setb.remove(new[0])
                        #get the index 
                        index = b.index(new[0])
                        if visited[index] : 
                            not_found = 0 
                            break 
                        #update the entry 
                        new[0] = a[index]
                        new[2] = min(new[2] , d[index])
                        visited[index] = True
                        
                    if new[1] in seta : 
                        seta.remove(new[1])
                        # get the index 
                        index =  a.index(new[1])
                        if visited[index] : 
                            not_found = 0 
                            break
                        #update the entry
                        new[1] = b[index]
                        new[2] = min(new[2] , d[index])
                        visited[index] = True 
                # if no loop found .. add the entry        
                if not_found and new[0] != new[1] : 
                    res.append(new)
        # sorting is for.. question purpose 
        res.sort()            
        return res 
            