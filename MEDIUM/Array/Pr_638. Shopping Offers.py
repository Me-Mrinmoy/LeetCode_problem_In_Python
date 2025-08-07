class Solution:
    def shoppingOffers(self, price, special, needs):
        n = len(price)
        memo = {}

        def dfs(current_needs):
            # Use tuple as key for memoization
            key = tuple(current_needs)
            if key in memo:
                return memo[key]

            # Base case: buying items without any offer
            total = sum(current_needs[i] * price[i] for i in range(n))

            # Try applying each special offer
            for offer in special:
                new_needs = []
                for i in range(n):
                    if offer[i] > current_needs[i]:
                        break  # Offer can't be applied
                    new_needs.append(current_needs[i] - offer[i])
                else:
                    # Offer is valid
                    total = min(total, offer[-1] + dfs(new_needs))

            memo[key] = total
            return total

        return dfs(needs)
