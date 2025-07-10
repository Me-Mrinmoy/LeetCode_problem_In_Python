class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        def maxSubsequence(nums, t):
            stack = []
            drop = len(nums) - t
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:t]

        def merge(seq1, seq2):
            res = []
            while seq1 or seq2:
                # compare remaining sequences lexicographically
                if seq1 > seq2:
                    res.append(seq1.pop(0))
                else:
                    res.append(seq2.pop(0))
            return res

        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            part1 = maxSubsequence(nums1, i)
            part2 = maxSubsequence(nums2, k - i)
            candidate = merge(part1[:], part2[:])  # use slices to avoid mutation
            if candidate > max_result:
                max_result = candidate

        return max_result
