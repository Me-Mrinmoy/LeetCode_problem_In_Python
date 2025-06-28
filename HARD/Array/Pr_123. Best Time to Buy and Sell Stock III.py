class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        first_buy = float('inf')  # Minimum price for the first buy
        first_profit = 0           # Maximum profit after the first transaction
        
        second_buy = float('inf')  # Minimum price for the second buy
        second_profit = 0           # Maximum profit after the second transaction
        
        for price in prices:
            # Update first_buy and first_profit
            first_buy = min(first_buy, price)  # Minimum price for the first buy
            first_profit = max(first_profit, price - first_buy)  # Max profit after the first transaction
            
            # Update second_buy and second_profit
            second_buy = min(second_buy, price - first_profit)  # Effective buy price considering first transaction profit
            second_profit = max(second_profit, price - second_buy)  # Max profit after the second transaction
            
        return second_profit

# Example usage
if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(result)  # Output: 6
