class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # iterate through array
        # keep track of current lowest stock price in prices that have been processed
        # also keep track of the current highest possible sale
        # if current stock price less than lowest, set new lowest stock price
        # if currrent stock price is greater than lowest, calculate sale and update highest
        # return highest
        lowest_stock_price = float('inf')
        max_profit = 0

        for price in prices:
            max_profit = max(max_profit, price - lowest_stock_price)
            lowest_stock_price = min(lowest_stock_price, price)
        
        return max_profit