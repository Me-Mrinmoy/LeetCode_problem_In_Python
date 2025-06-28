class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')  # Initialize min_price to a very high value
        max_profit = 0  # Initialize max_profit to 0

        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price
            
            # Calculate potential profit
            profit = price - min_price
            
            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit

# Example usage
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)  # Output: 5
