import random

class Solution:
    def findKthLargest(self, nums, k):
        # Convert the problem into finding the (n-k)th smallest element
        target = len(nums) - k

        def quickselect(left, right):
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            pivot = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            nums[pivot], nums[right] = nums[right], nums[pivot]
            
            # Now, the pivot is at the correct position
            if pivot == target:
                return nums[pivot]
            elif pivot < target:
                return quickselect(pivot + 1, right)
            else:
                return quickselect(left, pivot - 1)

        return quickselect(0, len(nums) - 1)

# Example usage
solution = Solution()

# Example 1
nums1 = [3, 2, 1, 5, 6, 4]
k1 = 2
print(solution.findKthLargest(nums1, k1))  # Output: 5

# Example 2
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k2 = 4
print(solution.findKthLargest(nums2, k2))  # Output: 4
