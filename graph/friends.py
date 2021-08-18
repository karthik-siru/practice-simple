#approach : 
'''
 -> Compute the net amount for every person. 
    The net amount for person ‘i’ can be computed by subtracting sum of all debts from sum of all credits.
 -> Find the two persons that are maximum creditor and maximum debtor. 
 -> Let the maximum amount to be credited maximum creditor be maxCredit and maximum amount to be debited from maximum debtor be maxDebit.
 -> Let the maximum debtor be Pd and maximum creditor be Pc.
 -> Find the minimum of maxDebit and maxCredit.
 -> Let minimum of two be x. Debit ‘x’ from Pd and credit this amount to Pc
 -> If x is equal to maxCredit, then remove Pc from set of persons and
    recur for remaining (n-1) persons.
 -> If x is equal to maxDebit, then remove Pd from set of persons and 
    recur for remaining (n-1) persons.
'''

class Solution  :
    #returns the min-val index 
    def getMin(self, arr):
        index  = 0 
        min_val = arr[0]

        for i in range(len(arr)):
            if arr[i] < min_val : 
                min_val = arr[i]
                index = i 
        return index 
    #returns the max-val index 
    def getMax(self, arr):
        index  = 0 
        max_val = arr[0]

        for i in range(len(arr)):
            if arr[i] > max_val : 
                max_val = arr[i]
                index = i 
        return index 

    def minof2 (self, a, b):
        return a if a<b else b

    def minimiseFlowRec(self,amount ) : 
        # get max, min values from the amount 
        Credit =  self.getMax(amount)
        Debit  =  self.getMin(amount)
        
        # all debts cleared 
        if amount[Credit] ==0 and amount[Debit] == 0:
            return 0 
        
        min = self.minof2(-amount[Debit] , amount[Credit])
        # pay to the maxCreditor from maxDebitor
        amount[Credit] -= min
        amount[Debit]  += min 

        print(f"person {Debit}  pays {min} to {Credit} ")
        
        # recurse with remaining values.
        self.minimiseFlowRec(amount)


    def minimiseFlow(self, graph) : 
        # create a array which contians net amount 
        amount = [0 for i in range(graph.vertices)]

        for i in range(graph.vertices) : 
            for j in graph.adj[i] : 
                amount[i] += (graph[i][j] -  graph[j][i])

        self.minimiseFlowRec(amount)
