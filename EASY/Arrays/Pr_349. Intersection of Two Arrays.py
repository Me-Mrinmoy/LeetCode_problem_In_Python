class Solution:
    def intersection(self, nums1, nums2):
        # Convert both lists to sets and find the intersection
        result = set(nums1) & set(nums2)
        return list(result)
