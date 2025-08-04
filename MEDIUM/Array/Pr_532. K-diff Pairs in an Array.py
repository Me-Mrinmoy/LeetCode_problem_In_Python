from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0  # absolute difference can't be negative
        
        counter = Counter(nums)
        count = 0
        
        if k == 0:
            # Count numbers appearing more than once
            for num in counter:
                if counter[num] > 1:
                    count += 1
        else:
            # Check if num + k exists in the set
            for num in counter:
                if num + k in counter:
                    count += 1
        
        return count
