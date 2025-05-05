class Solution(object):
    def maxProfit(self, prices, fee):
        if not prices:
            return 0
        
        hold = -prices[0] # We buy on the first day
        cash = 0 # No profit initially

        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)
        
        return cash
