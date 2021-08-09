'''
Sort the elements according to their finishing times ,
and held a meeting whenever possible ;) 

'''
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        meetings = [] 
        
        for i in range(len(start)) :
            meetings.append([start[i] , end[i]])
            
        meetings.sort(key = lambda x :  x [1])
        
        count = 0
        end_time = -9999999
        
        for i in meetings : 
            if end_time < i[0] : 
                count +=1 
                end_time = i[1]
                
        return count 