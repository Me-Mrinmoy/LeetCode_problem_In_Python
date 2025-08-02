class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        
        # For elements with no greater element
        for num in stack:
            next_greater[num] = -1
        
        return [next_greater[num] for num in nums1]
