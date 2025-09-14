class Solution:
    def numMovesStonesII(self, stones: list[int]) -> list[int]:
        stones.sort()
        n = len(stones)
        high = max(stones[-1] - stones[1] + 1 - (n - 1), stones[-2] - stones[0] + 1 - (n - 1))
        idx, low = 0, n
        for i in range(n):
            while stones[i] - stones[idx] + 1 > n:
                idx += 1
            cnt = i - idx + 1
            if cnt == n - 1 and stones[i] - stones[idx] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - cnt)
        return [low, high]
