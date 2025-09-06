class Solution:
    def longestOnes(self, nums, k):
        left = 0
        max_length = 0
        zero_count = 0

        
        for right in range(len(nums)):
            
            if nums[right] == 0:
                zero_count += 1

            
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            
            max_length = max(max_length, right - left + 1)

        return max_length


nums1 = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k1 = 2

nums2 = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k2 = 3

solution = Solution()
print(solution.longestOnes(nums1, k1))  
print(solution.longestOnes(nums2, k2))  
