
# Question : 
'''
Schedule the jobs , with given deadlines and to obtain max profit ;) 
'''

#Approach : 
'''
Sort the jobs according to their profits in descending order  . 
Now , take the first job and add it to the profit and increase the count . 
->  Assign it in the deadline slot .  
->  For every job from 0  check upto when the job can wait and , free slots .
'''

class Solution : 
        
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,jobs,T):
        
        # code here
        
        profit = 0
        count = 0
     
        # list to store used and unused slots info
        slot = [-1] * T
     
        # arrange the jobs in decreasing order of their profits
        jobs.sort(key=lambda x: x.profit, reverse=True)
     
        # consider each job in decreasing order of their profits
        for job in jobs:
            # search for the next free slot and map the task to that slot
            for j in reversed(range(job.deadline)):
                if j < T and slot[j] == -1:
                    slot[j] = job.id
                    profit += job.profit
                    count +=  1
                    break
                
        return (count ,profit) 