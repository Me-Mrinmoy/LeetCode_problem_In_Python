class Solution:
    def maxProfit(self, prices):
        total_profit = 0
        
        # Iterate through the prices
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's price
            if prices[i] > prices[i - 1]:
                # Add the profit (difference) to total_profit
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)  # Output: 7
