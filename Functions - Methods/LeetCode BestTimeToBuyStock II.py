class Solution:
    def maxProfit(self, prices):
        total = 0
        
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                total+=(prices[i+1]-prices[i])
        return total
        
    #### Only 1 transaction
    def maxProfit(prices):
        min_price = float('inf')
        total = 0
    
        for i in prices:
            min_price = min(i,min_price)
            profit = i - min_price
            total = max(total,profit)
        return total
