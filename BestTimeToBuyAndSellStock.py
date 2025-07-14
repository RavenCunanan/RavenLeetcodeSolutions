class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf') #lowest price seen so far
        max_profit = 0 #highest profit seen so far profit equation is price - min_price

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
