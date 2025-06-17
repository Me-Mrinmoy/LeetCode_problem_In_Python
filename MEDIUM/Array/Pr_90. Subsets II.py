class Solution:
    def subsetsWithDup(self, nums):
        
        nums.sort()
        result = []
        subset = []
        
        def backtrack(start):
            
            result.append(subset[:])
            
            for i in range(start, len(nums)):
                
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                subset.append(nums[i])
                
                backtrack(i + 1)
                
                subset.pop()
        
        backtrack(0)
        return result


solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))  
print(solution.subsetsWithDup([0]))        
