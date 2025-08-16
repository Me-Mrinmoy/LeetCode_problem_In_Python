class Solution:
    def minSwap(self, nums1, nums2):
        n = len(nums1)
        # swap[i]: min swaps up to i if we swap at i
        # keep[i]: min swaps up to i if we do not swap at i
        swap = [float('inf')] * n
        keep = [float('inf')] * n

        keep[0] = 0
        swap[0] = 1

        for i in range(1, n):
            if nums1[i] > nums1[i-1] and nums2[i] > nums2[i-1]:
                keep[i] = keep[i-1]
                swap[i] = swap[i-1] + 1
            if nums1[i] > nums2[i-1] and nums2[i] > nums1[i-1]:
                keep[i] = min(keep[i], swap[i-1])
                swap[i] = min(swap[i], keep[i-1] + 1)

        return min(keep[-1], swap[-1])
