class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta = (sumB - sumA) // 2
        setB = set(bobSizes)

        for x in aliceSizes:
            if x + delta in setB:
                return [x, x + delta]
