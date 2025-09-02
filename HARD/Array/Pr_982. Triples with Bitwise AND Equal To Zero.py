class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            for j in nums:
                d[i&j] = d.setdefault(i&j, 0) + 1
        A = 0
        for ans, count in d.items():
            for num in nums:
                if ans&num == 0:
                    A += count
        return A
