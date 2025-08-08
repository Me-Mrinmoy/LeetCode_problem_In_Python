class Solution:
    def judgePoint24(self, cards):
        EPS = 1e-6
        
        def backtrack(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            
            # Try all pairs
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Remaining numbers after picking i and j
                        next_nums = []
                        for k in range(len(nums)):
                            if k != i and k != j:
                                next_nums.append(nums[k])
                        
                        # Try all operations
                        for op in [
                            nums[i] + nums[j],
                            nums[i] - nums[j],
                            nums[j] - nums[i],
                            nums[i] * nums[j]
                        ]:
                            next_nums.append(op)
                            if backtrack(next_nums):
                                return True
                            next_nums.pop()
                        
                        # Division cases
                        if abs(nums[j]) > EPS:
                            next_nums.append(nums[i] / nums[j])
                            if backtrack(next_nums):
                                return True
                            next_nums.pop()
                        if abs(nums[i]) > EPS:
                            next_nums.append(nums[j] / nums[i])
                            if backtrack(next_nums):
                                return True
                            next_nums.pop()
            return False
        
        return backtrack([float(c) for c in cards])
