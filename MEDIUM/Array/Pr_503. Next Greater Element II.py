class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        # Traverse the array twice to simulate circularity
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]
            # Maintain decreasing stack: pop smaller elements
            while stack and nums[stack[-1]] <= current:
                stack.pop()
            # If we are in the first pass, update result
            if i < n:
                if stack:
                    res[i] = nums[stack[-1]]
            # Push current index
            stack.append(i % n)

        return res
