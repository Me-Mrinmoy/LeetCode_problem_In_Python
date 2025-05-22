class Solution:
    def permuteUnique(self, nums):
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])  # Append a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[start]:
                    continue
                
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)  # Recurse
                # Backtrack (swap back)
                nums[start], nums[i] = nums[i], nums[start]

        nums.sort()  # Sort the numbers to handle duplicates
        result = []
        backtrack(0)
        return result

# Example usage:
solution = Solution()
print(solution.permuteUnique([1, 1, 2]))  # Output: [[1,1,2],[1,2,1],[2,1,1]]
print(solution.permuteUnique([1, 2, 3]))  # Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
