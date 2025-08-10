class Solution:
    def fallingSquares(self, positions):
        ans = []
        squares = []  # stores (start, end, height)
        max_height = 0

        for left, size in positions:
            right = left + size
            base_height = 0

            # Check all existing squares for overlap
            for l, r, h in squares:
                if not (right <= l or left >= r):  # Overlap condition
                    base_height = max(base_height, h)

            new_height = base_height + size
            squares.append((left, right, new_height))
            max_height = max(max_height, new_height)
            ans.append(max_height)

        return ans
