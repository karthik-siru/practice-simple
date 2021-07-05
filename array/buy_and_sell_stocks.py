def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)< 2 :
            return 0
        
        max_profit = 0
        
        buy = -1
        sell = -1
        
        min_value = prices[0]
        
        for i in range(len(prices)):           
            if prices[i] < min_value :
                buy = i 
                min_value = prices[i] 
            if max_profit < prices[i]-min_value :
                max_profit = prices[i]-min_value
                sell = i 
        return max_profit
