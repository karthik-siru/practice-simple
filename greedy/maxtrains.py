#Question : 
'''
 Given the trains schedule .. how many max trains can stop . at the 
 platform ...

 ->  Train stops...  only if the platform is free .
'''

class Solution : 

    def maxTrains (self, trains) :
        # sort the trains acc to their depature time .
        trains.sort(key = lambda x :  x.departure)
        
        inf = 99999999
        trainsCount = 0
        endTime = -inf 
        
        # whenever possible , try  to schedule a train ;).
        for train in trains :
            arrival = train.arrival 
            departure = train.departure 
            # endTime < arrival -- 
            # train comes after prev train departs 
            if endTime < arrival : 
                endTime = departure 
                trainsCount += 1 

        return trainsCount 
