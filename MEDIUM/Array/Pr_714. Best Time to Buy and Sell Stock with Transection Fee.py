class Solution:
    def maxProfit(self, prices, fee):
        hold = -prices[0]     # Bought on day 0
        cash = 0              # No stock on day 0

        for price in prices[1:]:
            # Update cash first (sell action)
            cash = max(cash, hold + price - fee)
            # Update hold next (buy action)
            hold = max(hold, cash - price)

        return cash
