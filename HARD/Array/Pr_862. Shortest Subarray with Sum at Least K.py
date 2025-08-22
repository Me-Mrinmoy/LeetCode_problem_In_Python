from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        
        # build prefix sum
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        ans = n + 1
        dq = deque()  # store indices of prefix
        
        for j in range(n + 1):
            # check if we can pop from front
            while dq and prefix[j] - prefix[dq[0]] >= k:
                ans = min(ans, j - dq.popleft())
            
            # maintain monotonic increasing deque
            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
            
            dq.append(j)
        
        return ans if ans <= n else -1
