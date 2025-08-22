class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        def canEat(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours <= h

        while left < right:
            mid = (left + right) // 2
            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left
