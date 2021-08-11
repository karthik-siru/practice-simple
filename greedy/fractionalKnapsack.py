    def fractionalknapsack(self, W,Items,n):
        
        # code here
        Items.sort(key  =  lambda x  : x.value , reverse = True )
        
        profit = 0
        
        for item in Items : 
            if W-item.weight >= 0 :
                W -= item.weight 
                profit += item.value 
            else :
                profit += (W /item.weight)*(item.value)
                break 
            
        return profit 
                