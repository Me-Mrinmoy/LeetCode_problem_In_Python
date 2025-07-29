from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        count = 0
        sum_map = defaultdict(int)
        
        # Store sums of all pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
        
        # Check if complement exists in sum_map for sums from nums3 and nums4
        for c in nums3:
            for d in nums4:
                complement = -(c + d)
                count += sum_map.get(complement, 0)
        
        return count

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]

    print("Output:", sol.fourSumCount(nums1, nums2, nums3, nums4))  # Output: 2
