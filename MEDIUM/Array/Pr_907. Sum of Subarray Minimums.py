class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        # Previous Less Element (strictly less)
        ple = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)

        # Next Less Element (less or equal)
        nle = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)

        # Contribution
        ans = 0
        for i in range(n):
            ans += arr[i] * (i - ple[i]) * (nle[i] - i)
            ans %= MOD
        return ans
