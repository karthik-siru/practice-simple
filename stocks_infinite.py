'''

Best time to sell and buy the stock with as many transactions possible 

Valley-Peak approach 

'''

def stocks_infinte (prices ):
       profit = 0
       
       for i in range (1 , len(prices)) :
            # add to the profit if it is a peak 
            if prices[i] - prices[i-1] :
                   profit +=  prices[i]- prices[i-1]
                
       return profit 
