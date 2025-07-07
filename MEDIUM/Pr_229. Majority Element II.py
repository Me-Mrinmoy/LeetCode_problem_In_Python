class Solution:
    def majorityElement(self, nums):
        # Step 1: Find the two potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Verify the candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Step 3: Collect the result
        result = []
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        
        return result

# Example usage
solution = Solution()

# Example 1
nums1 = [3, 2, 3]
print(solution.majorityElement(nums1))  # Output: [3]

# Example 2
nums2 = [1]
print(solution.majorityElement(nums2))  # Output: [1]

# Example 3
nums3 = [1, 2]
print(solution.majorityElement(nums3))  # Output: [1, 2]
