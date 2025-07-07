class Solution:
    def summaryRanges(self, nums):
        result = []
        
        if not nums:
            return result
        
        start = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))
                start = nums[i]
        
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))
        
        return result


# Example usage:
sol = Solution()
print(sol.summaryRanges([0, 1, 2, 4, 5, 7]))      # Output: ["0->2", "4->5", "7"]
print(sol.summaryRanges([0, 2, 3, 4, 6, 8, 9]))   # Output: ["0", "2->4", "6", "8->9"]
