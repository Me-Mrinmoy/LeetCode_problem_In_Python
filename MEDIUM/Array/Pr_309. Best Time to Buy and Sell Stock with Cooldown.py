class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            hold = max(hold, rest - price)
            rest = max(rest, sold)
            sold = prev_hold + price

        return max(sold, rest)
