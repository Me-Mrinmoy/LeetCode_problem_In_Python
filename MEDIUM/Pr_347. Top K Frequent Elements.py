from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        freq = Counter(nums)
        
        # Create buckets: index i holds list of numbers that appear i times
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        
        res = []
        # Traverse buckets in reverse order to get most frequent elements
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
