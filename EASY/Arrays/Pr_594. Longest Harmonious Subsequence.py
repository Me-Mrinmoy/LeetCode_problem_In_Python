class Solution:
    def findLHS(self, nums):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_len = 0
        for num in freq:
            if num + 1 in freq:
                max_len = max(max_len, freq[num] + freq[num + 1])
        return max_len
