class Solution:
    def candy(self, ratings):
        n = len(ratings)
        # Create an array to store the number of candies, initially each child gets 1 candy
        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # The total number of candies needed is the sum of the candies array
        return sum(candies)

# Example usage
solution = Solution()
ratings = [1, 0, 2]
result = solution.candy(ratings)
print(result)  # Output: 5
