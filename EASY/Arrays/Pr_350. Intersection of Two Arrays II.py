from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        # Count the frequency of elements in both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        result = []
        for num in count1:
            if num in count2:
                # Add the element min(count1, count2) times
                result.extend([num] * min(count1[num], count2[num]))
        
        return result
