class Solution:
    def advantageCount(self, nums1, nums2):
        n = len(nums1)
        
        # sort nums1
        nums1.sort()
        
        # sort nums2 but keep original indices
        sorted_nums2 = sorted([(val, i) for i, val in enumerate(nums2)])
        
        res = [0] * n
        lo, hi = 0, n - 1
        
        for num in nums1:
            if num > sorted_nums2[lo][0]:
                # beat the smallest in nums2
                _, idx = sorted_nums2[lo]
                res[idx] = num
                lo += 1
            else:
                # sacrifice against the largest
                _, idx = sorted_nums2[hi]
                res[idx] = num
                hi -= 1
        
        return res
