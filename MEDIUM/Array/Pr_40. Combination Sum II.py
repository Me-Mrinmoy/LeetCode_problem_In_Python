class Solution:
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()  # Sort the candidates to facilitate the handling of duplicates
        self.backtrack(candidates, target, [], result, 0)
        return result

    def backtrack(self, candidates, target, current_combination, result, start):
        if target == 0:
            result.append(list(current_combination))  # Found a valid combination
            return
        if target < 0:
            return  # Exceeded the target
        
        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            current_combination.append(candidates[i])  # Choose the candidate
            self.backtrack(candidates, target - candidates[i], current_combination, result, i + 1)  # Move to the next index
            current_combination.pop()  # Backtrack to try another candidate

# Example usage:
solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
output = solution.combinationSum2(candidates, target)
print(output)
