from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        
        n = len(nums)
        result = []
        deq = deque()  # This will store indices of the elements in nums

        for i in range(n):
            # Remove indices that are out of the bounds of the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # Remove indices from the back of the deque while the current element is greater
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # Add the current index to the deque
            deq.append(i)
            
            # The first index of the deque is the maximum for the current window
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result

# Example usage:
solution = Solution()
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print(solution.maxSlidingWindow(nums1, k1))  # Output: [3, 3, 5, 5, 6, 7]

nums2 = [1]
k2 = 1
print(solution.maxSlidingWindow(nums2, k2))  # Output: [1]
