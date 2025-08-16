class Solution:
    def bestRotation(self, nums):
        n = len(nums)
        change = [0] * (n + 1)

        for i, num in enumerate(nums):
            # Range of valid rotations where this num contributes a point
            low = (i + 1) % n
            high = (i - num + n + 1) % n

            change[low] += 1
            change[high] -= 1

            if low >= high:
                change[0] += 1

        best_k = 0
        score = 0
        max_score = -1

        for k in range(n):
            score += change[k]
            if score > max_score:
                max_score = score
                best_k = k

        return best_k
