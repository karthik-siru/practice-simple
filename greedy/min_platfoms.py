#question  : 
'''
Given arrival and departure times of all trains that reach a railway station.
Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day.
Arrival and departure time can never be the same for a train but we can have arrival time
of one train equal to departure time of the other. 
At any given instance of time, same platform can not be used for both departure of a train 
and arrival of another train. In such cases, we need different platforms.
'''

#approach  (my approach ) :
'''
Sort the trains according to their departure time . 

-> Now as done in activity selection problem .. we will keep track of end time 
-> And If any train's arrival is after endTime .. we don't need a platform
-> we will update the endTime . 
-> after one iteration , we are left with trains that doesnot fit in platform 1 
-> So , we will do the same thing ..until no train left .p;)

-> Bit lengthy .. now see the second approach . 
''' 

#approach (GFG) :
'''
Algorithm:

-> Sort the arrival and departure times of trains.
-> Create two pointers i=0, and j=0 and a variable to store ans 
   and current count plat
-> Run a loop while i<n and j<n and compare the ith element of arrival array
   and jth element of departure array.
-> If the arrival time is less than or equal to departure
   then one more platform is needed so increase the count, 
   i.e. plat++ and increment i
-> Else if the arrival time greater than departure 
   then one less platform is needed so decrease the count, 
   i.e. plat– and increment j
-> Update the ans, i.e ans = max(ans, plat).
'''


class Solution : 
    def findPlatform(self,arr, dep, n):
        # Sort arrival and
        # departure arrays
        arr.sort()
        dep.sort()

        plat_needed = 1
        result = 1
        i = 1
        j = 0
    
        while (i < n and j < n):
    
            # If next event in sorted
            # order is arrival,
            # increment count of
            # platforms needed
            if (arr[i] <= dep[j]):
    
                plat_needed += 1
                i += 1
    
            # Else decrement count
            # of platforms needed
            elif (arr[i] > dep[j]):
    
                plat_needed -= 1
                j += 1
    
            # Update result if needed
            if (plat_needed > result):
                result = plat_needed
    
        return result